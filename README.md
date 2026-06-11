# Chatbot AprendeAí

> Projeto de chatbot conversacional desenvolvido para o site institucional da **AprendeAí (Digital Learning)** como parte de projeto de extensão universitária.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Streamlit](https://img.shields.io/badge/Streamlit-Online-ff6a00?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Funcionando-brightgreen)
![ODS](https://img.shields.io/badge/ODS%204-Educação%20de%20Qualidade-orange)

---

## Acesso rápido

| Recurso | Link |
|---|---|
| Chatbot online | [Acessar](https://chabot-aprendeai-ugpp6ckmsyhwb6yjsa5eqc.streamlit.app) |
| Demonstração em vídeo | [Assistir](https://youtu.be/HImDkaQIpGM) |
| Repositório | [GitHub](https://github.com/ClintSant/PEX-DATASCIENCE-CHABOT-APRENDEAI) |

---

## Sobre o projeto

Este projeto foi desenvolvido como **Projeto de Extensão Universitária** para o site [aprendeai.com](https://www.aprendeai.com), empresa do setor de educação corporativa que oferece cursos digitais nas áreas de RH, Vendas, Financeiro e Marketing.

O chatbot atende três públicos distintos identificados no levantamento de requisitos realizado com o proprietário da empresa:

| Público | Objetivo |
|---|---|
| Empresa interessada | Capturar lead qualificado para o time comercial |
| Cliente / Colaborador | Resolver dúvidas técnicas sem atendimento humano |
| Visitante geral | Informar sobre catálogo, formatos e direcionar para vendedor |

---

## Contexto acadêmico

- **Tipo:** Projeto de Extensão Universitária
- **Eixo temático:** Educação de Qualidade — [ODS 4 da ONU](https://brasil.un.org/pt-br/sdgs/4)
- **Curso:** Ciência de Dados
- **Empresa parceira:** Digital Learning (AprendeAí) — fundada em 2016
- **Discente:** Clinton Gonçalves dos Santos — RA 2436178

---

## Fluxograma do chatbot

![Fluxograma do Chatbot](docs/fluxograma_chatbot.svg)

Legenda:
- Azul — Fluxo de empresa interessada em contratar
- Verde — Fluxo de cliente/colaborador (suporte técnico)
- Laranja — Fluxo de outras dúvidas (informacional)
- Roxo — Ações do sistema (envio de dados, webhook)
- Vermelho — Fim de conversa

---

## Demonstração

- [Acesse o chatbot online](https://chabot-aprendeai-ugpp6ckmsyhwb6yjsa5eqc.streamlit.app)
- [Assista ao chatbot funcionando](https://youtu.be/HImDkaQIpGM)

---

## Stack técnica

- **Backend:** Python 3.11 + Flask 3.0
- **Frontend local:** HTML5 + CSS3 + JavaScript (sem frameworks)
- **Deploy:** Streamlit Cloud (gratuito)
- **Arquitetura:** Máquina de estados em Python puro
- **CORS:** Flask-CORS para integração futura com Framer

---

## Estrutura do projeto

chatbot_aprendeai/
├── app.py                  # Servidor Flask (versão local)
├── fluxo.py                # Lógica dos 3 ramos conversacionais
├── streamlit_app.py        # Interface Streamlit (versão deploy)
├── requirements.txt        # Dependências
├── widget.js               # Widget embeddável para o site Framer
├── .python-version         # Versão do Python para o Streamlit Cloud
├── templates/
│   └── index.html          # Interface visual local do chat
└── docs/
└── fluxograma_chatbot.svg



---

## Fluxos implementados

**Ramo 1 — Empresa interessada**

O visitante informa sua necessidade (cursos LMS ou acessos na plataforma), nome, e-mail corporativo, telefone, área de atuação e número de colaboradores. Ao finalizar, o time comercial recebe os dados para contato.

**Ramo 2 — Cliente / Colaborador**

FAQ inline para os 3 problemas mais frequentes: acesso, certificado e senha. Se não resolver, escala para formulário de suporte com envio para contato@aprendeai.com.

**Ramo 3 — Outras dúvidas**

Respostas sobre catálogo, formatos e valores. Preços nunca são informados pelo bot — sempre redirecionado para consultor comercial.

---

## Métricas de sucesso previstas

- Número de leads gerados por mês
- Taxa de conversão de conversa para contato comercial
- Percentual de dúvidas técnicas resolvidas sem humano
- Taxa de abandono do chat
- NPS do atendimento

---

## Próximos passos para produção

- [ ] Integração webhook com CRM da empresa
- [ ] Inserção do widget.js no site Framer
- [ ] Tracking de eventos no Google Analytics
- [ ] Enriquecimento com LLM para dúvidas abertas

---

## Licença

Projeto desenvolvido para fins acadêmicos. Todos os direitos da marca AprendeAí pertencem à Digital Learning.

---

Desenvolvido como projeto de extensão universitária — Ciência de Dados
