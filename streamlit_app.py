import streamlit as st
from fluxo import processar_mensagem

st.set_page_config(
    page_title="Assistente AprendeAi",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .header-box {
        background-color: #ff6a00;
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 16px;
    }
    .header-box h3 { color: white; margin: 0; font-size: 16px; }
    .header-box p { color: rgba(255,255,255,0.85); margin: 0; font-size: 12px; }
    .dot {
        width: 8px; height: 8px; background: #4ade80;
        border-radius: 50%; display: inline-block; margin-right: 4px;
    }
    div[data-testid="stChatMessage"] {
        background-color: #ffffff !important;
        color: #1f2937 !important;
        border-radius: 12px;
        margin-bottom: 8px;
        padding: 8px;
    }
    div[data-testid="stChatMessage"] p {
        color: #1f2937 !important;
    }
    div[data-testid="stChatMessage"] * {
        color: #1f2937 !important;
    }
    .stButton button {
        background-color: white !important;
        border: 2px solid #ff6a00 !important;
        color: #ff6a00 !important;
        border-radius: 20px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }
    .stButton button:hover {
        background-color: #ff6a00 !important;
        color: white !important;
    }
</style>
<div class="header-box">
    <h3>Assistente AprendeAi</h3>
    <p><span class="dot"></span>Online agora</p>
</div>
""", unsafe_allow_html=True)

if "sessao" not in st.session_state:
    st.session_state.sessao = {}

if "historico" not in st.session_state:
    st.session_state.historico = []

if "opcoes_ativas" not in st.session_state:
    st.session_state.opcoes_ativas = []

if "iniciou" not in st.session_state:
    respostas, sessao_nova = processar_mensagem("", {})
    st.session_state.sessao = sessao_nova
    for bloco in respostas:
        if bloco["tipo"] == "texto":
            st.session_state.historico.append({
                "role": "assistant",
                "content": bloco["conteudo"]
            })
        elif bloco["tipo"] == "botoes":
            st.session_state.opcoes_ativas = bloco["opcoes"]
    st.session_state.iniciou = True

for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(f"<p style='color:#1f2937;margin:0;'>{msg['content']}</p>", unsafe_allow_html=True)

if st.session_state.opcoes_ativas:
    opcoes = st.session_state.opcoes_ativas
    cols = st.columns(len(opcoes))
    for i, opcao in enumerate(opcoes):
        with cols[i]:
            if st.button(opcao, key=f"btn_{opcao}_{len(st.session_state.historico)}"):
                st.session_state.historico.append({
                    "role": "user",
                    "content": opcao
                })
                st.session_state.opcoes_ativas = []
                respostas, sessao_nova = processar_mensagem(opcao, st.session_state.sessao)
                st.session_state.sessao = sessao_nova
                for bloco in respostas:
                    if bloco["tipo"] == "texto":
                        st.session_state.historico.append({
                            "role": "assistant",
                            "content": bloco["conteudo"]
                        })
                    elif bloco["tipo"] == "botoes":
                        st.session_state.opcoes_ativas = bloco["opcoes"]
                st.rerun()

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.historico.append({
        "role": "user",
        "content": prompt
    })
    st.session_state.opcoes_ativas = []
    respostas, sessao_nova = processar_mensagem(prompt, st.session_state.sessao)
    st.session_state.sessao = sessao_nova
    for bloco in respostas:
        if bloco["tipo"] == "texto":
            st.session_state.historico.append({
                "role": "assistant",
                "content": bloco["conteudo"]
            })
        elif bloco["tipo"] == "botoes":
            st.session_state.opcoes_ativas = bloco["opcoes"]
    st.rerun()
