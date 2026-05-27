# Chatbot AprendeAi

> Projeto de chatbot conversacional desenvolvido para o site institucional da **AprendeAi (Digital Learning)** como parte de projeto de extensao universitaria.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Status](https://img.shields.io/badge/Status-Funcionando-brightgreen)
![ODS](https://img.shields.io/badge/ODS%204-Educacao%20de%20Qualidade-orange)

---

## Sobre o projeto

Este projeto foi desenvolvido como **Projeto de Extensão** para o site [aprendeai.com](https://www.aprendeai.com), empresa do setor de educacao corporativa que oferece cursos digitais nas areas de RH, Vendas, Financeiro e Marketing.

O chatbot atende tres publicos distintos identificados no levantamento de requisitos realizado com o proprietario da empresa:

| Publico | Objetivo |
|---|---|
| Empresa interessada | Capturar lead qualificado para o time comercial |
| Cliente / Colaborador | Resolver duvidas tecnicas sem atendimento humano |
| Visitante geral | Informar sobre catalogo, formatos e direcionar para vendedor |

---

## Contexto academico

- **Tipo:** Projeto de Extensao Universitaria
- **Eixo tematico:** Educacao de Qualidade — [ODS 4 da ONU](https://brasil.un.org/pt-br/sdgs/4)
- **Curso:** Ciencia de Dados
- **Empresa parceira:** Digital Learning (AprendeAi) — fundada em 2016

---

## Fluxograma do chatbot

![Fluxograma do Chatbot](docs/fluxograma_chatbot.svg)

Legenda:
- Azul — Fluxo de empresa interessada em contratar
- Verde — Fluxo de cliente/colaborador (suporte tecnico)
- Laranja — Fluxo de outras duvidas (informacional)
- Roxo — Acoes do sistema (envio de dados, webhook)
- Vermelho — Fim de conversa

---

## Demonstração

[Assista ao chatbot funcionando]((https://youtu.be/HImDkaQIpGM))

---

## Stack técnica

- **Backend:** Python 3.11 + Flask 3.0
- **Frontend:** HTML5 + CSS3 + JavaScript (sem frameworks)
- **Arquitetura:** API REST stateless + maquina de estados no frontend
- **CORS:** Flask-CORS para integracao futura com Framer

---

## Estrutura do projeto

chatbot_aprendeai/
├── app.py                  # Servidor Flask
├── fluxo.py                # Logica dos 3 ramos conversacionais
├── requirements.txt        # Dependencias
├── widget.js               # Widget embeddavel para o site Framer
├── templates/
│   └── index.html          # Interface visual do chat
└── docs/
└── fluxograma_chatbot.svg


---

## Como executar localmente

**Pre-requisitos**
- Python 3.11+
- pip

**Instalacao**

```bash
git clone https://github.com/ClintSant/PEX-DATASCIENCE-CHABOT-APRENDEAI.git
cd PEX-DATASCIENCE-CHABOT-APRENDEAI/chatbot_aprendeai
pip install -r requirements.txt
python app.py
```

**Acesso**

http://127.0.0.1:5000



## Fluxos implementados

**Ramo 1 — Empresa interessada**

O visitante informa sua necessidade (cursos LMS ou acessos na plataforma), nome, e-mail corporativo, telefone, area de atuacao e numero de colaboradores. Ao finalizar, o time comercial recebe os dados para contato.

**Ramo 2 — Cliente / Colaborador**

FAQ inline para os 3 problemas mais frequentes: acesso, certificado e senha. Se nao resolver, escala para formulario de suporte com envio para contato@aprendeai.com.

**Ramo 3 — Outras duvidas**

Respostas sobre catalogo, formatos e valores. Precos nunca sao informados pelo bot — sempre redirecionado para consultor comercial.

---

## Metricas de sucesso previstas

- Numero de leads gerados por mes
- Taxa de conversao de conversa para contato comercial
- Percentual de duvidas tecnicas resolvidas sem humano
- Taxa de abandono do chat
- NPS do atendimento

---

## Proximos passos para producao

- [ ] Deploy em servidor publico
- [ ] Integracao webhook com CRM da empresa
- [ ] Insercao do widget.js no site Framer
- [ ] Tracking de eventos no Google Analytics
- [ ] Enriquecimento com LLM para duvidas abertas

---

## Licença

Projeto desenvolvido para fins academicos. Todos os direitos da marca AprendeAi pertencem a Digital Learning.

---

Desenvolvido como projeto de extensao universitaria — Ciencia de Dados
