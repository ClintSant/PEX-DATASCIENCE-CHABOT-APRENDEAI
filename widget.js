/**
 * Chatbot AprendeAi — Widget para Framer
 *
 * COMO USAR:
 * 1. Faça o deploy da API no Render
 * 2. Substitua API_URL abaixo pelo endereço gerado pelo Render
 * 3. Cole este script no Framer em: Site Settings → Custom Code → End of <body>
 */

(function () {

  // ─── CONFIGURAÇÃO ──────────────────────────────────────────────
  const API_URL = "https://activate-grunge-exert.ngrok-free.app/chat";
  // Substitua pela URL real após o deploy no Render
  // Exemplo: "https://chatbot-aprendeai.onrender.com/chat"
  // ────────────────────────────────────────────────────────────────

  let sessao = {};
  let aberto = false;

  // ─── ESTILOS ────────────────────────────────────────────────────
  const style = document.createElement("style");
  style.textContent = `
    #aprendeai-widget * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; }

    #aprendeai-btn {
      position: fixed;
      bottom: 28px;
      right: 28px;
      width: 58px;
      height: 58px;
      background: #ff6a00;
      border-radius: 50%;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 16px rgba(255,106,0,0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9998;
      transition: transform 0.2s, background 0.2s;
    }
    #aprendeai-btn:hover { transform: scale(1.08); background: #e55d00; }
    #aprendeai-btn svg { width: 26px; height: 26px; fill: #fff; }

    #aprendeai-badge {
      position: absolute;
      top: -4px;
      right: -4px;
      width: 18px;
      height: 18px;
      background: #ef4444;
      border-radius: 50%;
      font-size: 10px;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      display: none;
    }

    #aprendeai-chat {
      position: fixed;
      bottom: 100px;
      right: 28px;
      width: 380px;
      height: 560px;
      background: #fff;
      border-radius: 16px;
      box-shadow: 0 8px 40px rgba(0,0,0,0.16);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 9999;
      opacity: 0;
      transform: translateY(20px) scale(0.95);
      pointer-events: none;
      transition: opacity 0.25s, transform 0.25s;
    }
    #aprendeai-chat.aberto {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: all;
    }

    #aprendeai-header {
      background: #ff6a00;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    #aprendeai-header .avatar {
      width: 38px; height: 38px;
      background: rgba(255,255,255,0.2);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px; flex-shrink: 0;
    }
    #aprendeai-header .info h3 { color: #fff; font-size: 14px; font-weight: 600; }
    #aprendeai-header .info p  { color: rgba(255,255,255,0.85); font-size: 11px; margin-top: 2px; }
    #aprendeai-header .dot { width: 7px; height: 7px; background: #4ade80; border-radius: 50%; display: inline-block; margin-right: 4px; }
    #aprendeai-fechar {
      margin-left: auto; background: none; border: none;
      color: #fff; font-size: 20px; cursor: pointer; opacity: 0.8; line-height: 1;
    }
    #aprendeai-fechar:hover { opacity: 1; }

    #aprendeai-msgs {
      flex: 1; overflow-y: auto; padding: 16px 14px;
      display: flex; flex-direction: column; gap: 8px;
      background: #f8f9fa;
    }
    #aprendeai-msgs::-webkit-scrollbar { width: 3px; }
    #aprendeai-msgs::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

    .apai-msg {
      max-width: 80%; padding: 9px 13px;
      border-radius: 14px; font-size: 13px; line-height: 1.5;
      animation: apai-in 0.2s ease; white-space: pre-line;
    }
    @keyframes apai-in {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .apai-msg.bot {
      background: #fff; color: #1f2937;
      border-bottom-left-radius: 4px; align-self: flex-start;
      box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    }
    .apai-msg.usuario {
      background: #ff6a00; color: #fff;
      border-bottom-right-radius: 4px; align-self: flex-end;
    }

    .apai-opcoes {
      display: flex; flex-wrap: wrap; gap: 6px;
      align-self: flex-start; max-width: 90%;
      animation: apai-in 0.3s ease;
    }
    .apai-btn {
      background: #fff; border: 1.5px solid #ff6a00;
      color: #ff6a00; padding: 7px 13px; border-radius: 18px;
      font-size: 12px; font-weight: 500; cursor: pointer;
      transition: all 0.2s;
    }
    .apai-btn:hover { background: #ff6a00; color: #fff; }
    .apai-btn:disabled { opacity: 0.4; cursor: not-allowed; }

    .apai-typing {
      display: flex; gap: 4px; padding: 10px 13px;
      background: #fff; border-radius: 14px; border-bottom-left-radius: 4px;
      align-self: flex-start; box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    }
    .apai-typing span {
      width: 6px; height: 6px; background: #bbb;
      border-radius: 50%; animation: apai-bounce 1s infinite;
    }
    .apai-typing span:nth-child(2) { animation-delay: 0.15s; }
    .apai-typing span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes apai-bounce {
      0%,60%,100% { transform: translateY(0); }
      30%          { transform: translateY(-5px); }
    }

    #aprendeai-input-area {
      padding: 10px 12px; background: #fff;
      border-top: 1px solid #f0f0f0; display: flex; gap: 8px;
    }
    #aprendeai-input {
      flex: 1; border: 1px solid #e5e7eb; border-radius: 20px;
      padding: 9px 14px; font-size: 13px; outline: none;
      transition: border 0.2s;
    }
    #aprendeai-input:focus { border-color: #ff6a00; }
    #aprendeai-enviar {
      background: #ff6a00; border: none; border-radius: 50%;
      width: 38px; height: 38px; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: background 0.2s; flex-shrink: 0;
    }
    #aprendeai-enviar:hover { background: #e55d00; }
    #aprendeai-enviar svg { width: 16px; height: 16px; fill: #fff; }

    @media (max-width: 440px) {
      #aprendeai-chat { width: calc(100vw - 24px); right: 12px; bottom: 90px; }
    }
  `;
  document.head.appendChild(style);

  // ─── HTML DO WIDGET ─────────────────────────────────────────────
  const wrapper = document.createElement("div");
  wrapper.id = "aprendeai-widget";
  wrapper.innerHTML = `
    <button id="aprendeai-btn" title="Fale com a AprendeAi">
      <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
      <span id="aprendeai-badge">1</span>
    </button>

    <div id="aprendeai-chat">
      <div id="aprendeai-header">
        <div class="avatar">🎓</div>
        <div class="info">
          <h3>Assistente AprendeAi</h3>
          <p><span class="dot"></span>Online agora</p>
        </div>
        <button id="aprendeai-fechar">✕</button>
      </div>

      <div id="aprendeai-msgs"></div>

      <div id="aprendeai-input-area">
        <input id="aprendeai-input" type="text" placeholder="Digite sua mensagem..." autocomplete="off"/>
        <button id="aprendeai-enviar">
          <svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2z"/></svg>
        </button>
      </div>
    </div>
  `;
  document.body.appendChild(wrapper);

  // ─── REFERÊNCIAS ────────────────────────────────────────────────
  const btnAbrir   = document.getElementById("aprendeai-btn");
  const chatBox    = document.getElementById("aprendeai-chat");
  const btnFechar  = document.getElementById("aprendeai-fechar");
  const msgArea    = document.getElementById("aprendeai-msgs");
  const inputEl    = document.getElementById("aprendeai-input");
  const btnEnviar  = document.getElementById("aprendeai-enviar");
  const badge      = document.getElementById("aprendeai-badge");

  let iniciou = false;

  // ─── ABRIR / FECHAR ─────────────────────────────────────────────
  btnAbrir.addEventListener("click", () => {
    aberto = true;
    chatBox.classList.add("aberto");
    badge.style.display = "none";
    inputEl.focus();
    if (!iniciou) {
      iniciou = true;
      enviar("", true);
    }
  });

  btnFechar.addEventListener("click", () => {
    aberto = false;
    chatBox.classList.remove("aberto");
  });

  // ─── ENVIAR MENSAGEM ────────────────────────────────────────────
  function enviarMensagem() {
    const texto = inputEl.value.trim();
    if (!texto) return;
    inputEl.value = "";
    adicionarMsg(texto, "usuario");
    enviar(texto, false);
  }

  btnEnviar.addEventListener("click", enviarMensagem);
  inputEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter") enviarMensagem();
  });

  async function enviar(mensagem, inicio) {
    desabilitarBtns(true);
    const typing = mostrarTyping();

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensagem, sessao })
      });
      const data = await res.json();
      sessao = data.sessao;
      typing.remove();

      for (let i = 0; i < data.resposta.length; i++) {
        await delay(i === 0 ? 0 : 350);
        renderBloco(data.resposta[i]);
      }

    } catch (err) {
      typing.remove();
      adicionarMsg("Erro de conexao. Tente novamente em instantes.", "bot");
    }

    desabilitarBtns(false);
    rolar();
  }

  function renderBloco(bloco) {
    if (bloco.tipo === "texto") {
      adicionarMsg(bloco.conteudo, "bot");
    } else if (bloco.tipo === "botoes") {
      const div = document.createElement("div");
      div.className = "apai-opcoes";
      bloco.opcoes.forEach(op => {
        const btn = document.createElement("button");
        btn.className = "apai-btn";
        btn.textContent = op;
        btn.onclick = () => {
          adicionarMsg(op, "usuario");
          div.querySelectorAll("button").forEach(b => b.disabled = true);
          enviar(op, false);
        };
        div.appendChild(btn);
      });
      msgArea.appendChild(div);
    }
    rolar();
  }

  function adicionarMsg(texto, tipo) {
    const el = document.createElement("div");
    el.className = `apai-msg ${tipo}`;
    el.textContent = texto;
    msgArea.appendChild(el);
    rolar();

    // Mostra badge se o chat estiver fechado e for mensagem do bot
    if (!aberto && tipo === "bot") {
      badge.style.display = "flex";
    }
  }

  function mostrarTyping() {
    const el = document.createElement("div");
    el.className = "apai-typing";
    el.innerHTML = "<span></span><span></span><span></span>";
    msgArea.appendChild(el);
    rolar();
    return el;
  }

  function desabilitarBtns(estado) {
    document.querySelectorAll(".apai-btn").forEach(b => {
      if (!b.disabled) b.disabled = estado;
    });
  }

  function rolar() {
    msgArea.scrollTop = msgArea.scrollHeight;
  }

  function delay(ms) {
    return new Promise(r => setTimeout(r, ms));
  }

})();
