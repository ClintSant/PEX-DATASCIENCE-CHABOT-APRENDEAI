import streamlit as st
from fluxo import processar_mensagem

# ── Configuração da página ──────────────────────────────────────
st.set_page_config(
    page_title="Assistente AprendeAi",
    page_icon="🎓",
    layout="centered"
)

# ── CSS customizado com cores da AprendeAi ──────────────────────
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    
    .header-box {
        background-color: #ff6a00;
        padding: 16px 20px;
        border-radius: 12px 12px 0 0;
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0;
    }
    .header-box h3 {
        color: white;
        margin: 0;
        font-size: 16px;
    }
    .header-box p {
        color: rgba(255,255,255,0.85);
        margin: 0;
        font-size: 12px;
    }
    .dot {
        width: 8px; height: 8px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        margin-right: 4px;
    }
    div[data-testid="stChatMessage"] {
        background: white;
        border-radius: 12px;
        margin-bottom: 8px;
    }
    .stButton button {
        background-color: white !important;
        border: 2px solid #ff6a00 !important;
        color: #ff6a00 !important;
        border-radius: 20px !important;
        padding: 6px 16px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
    }
    .stButton button:hover {
        background-color: #ff6a00 !important;
        color: white !important;
    }
    div[data-testid="stChatInputContainer"] {
        border-top: 1px solid #f0f0f0;
        padding-top: 8px;
    }
</style>

<div class="header-box">
    <div>
        <h3>Assistente AprendeAi</h3>
        <p><span class="dot"></span>Online agora</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Inicializar estado da sessão ────────────────────────────────
if "sessao" not in st.session_state:
    st.session_state.sessao = {}

if "historico" not in st.session_state:
    st.session_state.historico = []

if "opcoes_ativas" not in st.session_state:
    st.session_state.opcoes_ativas = []

if "iniciou" not in st.session_state:
    st.session_state.iniciou = False

# ── Função para processar e guardar resposta ────────────────────
def processar_e_guardar(mensagem):
    respostas, sessao_nova = processar_mensagem(mensagem, st.session_state.sessao)
    st.session_state.sessao = sessao_nova
    st.session_state.opcoes_ativas = []

    for bloco in respostas:
        if bloco["tipo"] == "texto":
            st.session_state.historico.append({
                "role": "assistant",
                "content": bloco["conteudo"],
                "tipo": "texto"
            })
        elif bloco["tipo"] == "botoes":
            st.session_state.opcoes_ativas = bloco["opcoes"]

# ── Iniciar conversa automaticamente ───────────────────────────
if not st.session_state.iniciou:
    processar_e_guardar("")
    st.session_state.iniciou = True

# ── Exibir histórico de mensagens ──────────────────────────────
for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── Exibir botões de opção ─────────────────────────────────────
if st.session_state.opcoes_ativas:
    cols = st.columns(len(st.session_state.opcoes_ativas))
    for i, opcao in enumerate(st.session_state.opcoes_ativas):
        with cols[i]:
            if st.button(opcao, key=f"btn_{opcao}"):
                # Registra escolha do usuário no histórico
                st.session_state.historico.append({
                    "role": "user",
                    "content": opcao,
                    "tipo": "texto"
                })
                processar_e_guardar(opcao)
                st.rerun()

# ── Input de texto livre ───────────────────────────────────────
if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.historico.append({
        "role": "user",
        "content": prompt,
        "tipo": "texto"
    })
    processar_e_guardar(prompt)
    st.rerun()
