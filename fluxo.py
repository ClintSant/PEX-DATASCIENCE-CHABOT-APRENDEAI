# fluxo.py — lógica completa do chatbot AprendeAí
# Baseado no fluxograma validado com o Fernando

def processar_mensagem(entrada, sessao):
    """
    Processa a mensagem do usuário e retorna a resposta do bot
    junto com o estado atualizado da sessão.

    sessao = {
        "etapa": string que identifica onde o usuário está no fluxo,
        "dados": dicionário com os dados coletados do lead
    }
    """
    entrada = entrada.strip()
    etapa = sessao.get("etapa", "inicio")
    dados = sessao.get("dados", {})

    # ==================== INÍCIO ====================
    if etapa == "inicio":
        sessao["etapa"] = "escolha_publica"
        return (
            [
                {"tipo": "texto", "conteudo": "Ola! Seja bem-vindo(a) a AprendeAi."},
                {"tipo": "texto", "conteudo": "Como posso ajudar voce hoje?"},
                {"tipo": "botoes", "opcoes": [
                    "Sou empresa interessada",
                    "Ja sou cliente ou colaborador",
                    "Outras duvidas"
                ]}
            ],
            sessao
        )

    # ==================== BIFURCAÇÃO PRINCIPAL ====================
    if etapa == "escolha_publica":
        if "empresa" in entrada.lower():
            sessao["etapa"] = "empresa_necessidade"
            return (
                [
                    {"tipo": "texto", "conteudo": "Otimo! Temos solucoes completas para empresas."},
                    {"tipo": "texto", "conteudo": "O que voce esta procurando?"},
                    {"tipo": "botoes", "opcoes": [
                        "Cursos prontos para o LMS da empresa",
                        "Acesso a plataforma AprendeAi para colaboradores"
                    ]}
                ],
                sessao
            )

        elif "cliente" in entrada.lower() or "colaborador" in entrada.lower():
            sessao["etapa"] = "cliente_problema"
            return (
                [
                    {"tipo": "texto", "conteudo": "Ola! Como posso te ajudar?"},
                    {"tipo": "botoes", "opcoes": [
                        "Nao consigo acessar meus cursos",
                        "Duvida sobre certificado",
                        "Esqueci minha senha",
                        "Outra duvida"
                    ]}
                ],
                sessao
            )

        elif "duvida" in entrada.lower() or "outra" in entrada.lower():
            sessao["etapa"] = "outras_duvidas"
            return (
                [
                    {"tipo": "texto", "conteudo": "Claro! Sobre o que voce gostaria de saber?"},
                    {"tipo": "botoes", "opcoes": [
                        "Catalogo de cursos",
                        "Formatos dos cursos",
                        "Valores e planos",
                        "Falar com um consultor"
                    ]}
                ],
                sessao
            )

        else:
            return (
                [
                    {"tipo": "texto", "conteudo": "Por favor, escolha uma das opcoes abaixo:"},
                    {"tipo": "botoes", "opcoes": [
                        "Sou empresa interessada",
                        "Ja sou cliente ou colaborador",
                        "Outras duvidas"
                    ]}
                ],
                sessao
            )

    # ==================== RAMO EMPRESA ====================
    if etapa == "empresa_necessidade":
        if "lms" in entrada.lower():
            dados["necessidade"] = "Cursos para LMS"
        else:
            dados["necessidade"] = "Acesso a plataforma"
        sessao["dados"] = dados
        sessao["etapa"] = "empresa_nome"
        return (
            [
                {"tipo": "texto", "conteudo": "Para conectar voce com nossos consultores, preciso de algumas informacoes."},
                {"tipo": "texto", "conteudo": "Qual o seu nome?"}
            ],
            sessao
        )

    if etapa == "empresa_nome":
        dados["nome"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "empresa_email"
        return (
            [{"tipo": "texto", "conteudo": "Qual o seu e-mail corporativo?"}],
            sessao
        )

    if etapa == "empresa_email":
        if "@" not in entrada:
            return (
                [{"tipo": "texto", "conteudo": "Por favor, insira um e-mail valido."}],
                sessao
            )
        dados["email"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "empresa_telefone"
        return (
            [{"tipo": "texto", "conteudo": "Qual o seu telefone com DDD?"}],
            sessao
        )

    if etapa == "empresa_telefone":
        dados["telefone"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "empresa_area"
        return (
            [{"tipo": "texto", "conteudo": "Qual a sua area de atuacao? (ex: RH, Vendas, Financeiro, Marketing)"}],
            sessao
        )

    if etapa == "empresa_area":
        dados["area"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "empresa_colaboradores"
        return (
            [{"tipo": "texto", "conteudo": "Quantos colaboradores a empresa possui?"}],
            sessao
        )

    if etapa == "empresa_colaboradores":
        dados["colaboradores"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "fim"

        # Aqui seria o ponto de integração com CRM ou e-mail
        # Por enquanto exibe os dados capturados no console
        print("\n===== NOVO LEAD CAPTURADO =====")
        for chave, valor in dados.items():
            print(f"{chave.upper()}: {valor}")
        print("================================\n")

        return (
            [
                {"tipo": "texto", "conteudo": "Perfeito! Nossos consultores entrarão em contato em breve."},
                {"tipo": "texto", "conteudo": "Obrigado pelo seu interesse na AprendeAi!"}
            ],
            sessao
        )

    # ==================== RAMO CLIENTE ====================
    if etapa == "cliente_problema":
        if "acesso" in entrada.lower() or "acessar" in entrada.lower():
            sessao["etapa"] = "cliente_acesso_empresa"
            return (
                [{"tipo": "texto", "conteudo": "Qual o nome da sua empresa?"}],
                sessao
            )

        elif "certificado" in entrada.lower():
            sessao["etapa"] = "cliente_certificado_resolveu"
            return (
                [
                    {"tipo": "texto", "conteudo": "Aqui estao as respostas mais frequentes sobre certificados:"},
                    {"tipo": "texto", "conteudo": (
                        "1. Onde encontro meu certificado?\n"
                        "   Acesse a area de Certificados no menu principal.\n\n"
                        "2. Meu nome nao esta completo no certificado\n"
                        "   Envie seu nome completo e e-mail para contato@aprendeai.com\n\n"
                        "3. Preciso do certificado mas nao esta disponivel\n"
                        "   O certificado fica disponivel apos concluir 80% do curso."
                    )},
                    {"tipo": "texto", "conteudo": "Isso resolveu sua duvida?"},
                    {"tipo": "botoes", "opcoes": ["Sim, resolveu", "Nao, preciso de mais ajuda"]}
                ],
                sessao
            )

        elif "senha" in entrada.lower():
            sessao["etapa"] = "cliente_senha_resolveu"
            return (
                [
                    {"tipo": "texto", "conteudo": (
                        "Para recuperar sua senha:\n"
                        "1. Acesse a tela de login\n"
                        "2. Clique em 'Esqueci minha senha'\n"
                        "3. Um link de recuperacao sera enviado para seu e-mail"
                    )},
                    {"tipo": "texto", "conteudo": "Isso resolveu sua duvida?"},
                    {"tipo": "botoes", "opcoes": ["Sim, resolveu", "Nao, preciso de mais ajuda"]}
                ],
                sessao
            )

        else:
            sessao["etapa"] = "escalonamento_nome"
            return (
                [
                    {"tipo": "texto", "conteudo": "Entendido! Vou conectar voce com nossa equipe de suporte."},
                    {"tipo": "texto", "conteudo": "Qual o seu nome?"}
                ],
                sessao
            )

    if etapa == "cliente_acesso_empresa":
        dados["empresa_cliente"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "cliente_acesso_resolveu"
        return (
            [
                {"tipo": "texto", "conteudo": "Tente os seguintes passos:"},
                {"tipo": "texto", "conteudo": (
                    "1. Limpe o cache do navegador\n"
                    "2. Tente acessar em outro navegador\n"
                    "3. Verifique se o e-mail de cadastro esta correto"
                )},
                {"tipo": "texto", "conteudo": "Isso resolveu?"},
                {"tipo": "botoes", "opcoes": ["Sim, resolveu", "Nao, preciso de mais ajuda"]}
            ],
            sessao
        )

    if etapa in ["cliente_acesso_resolveu", "cliente_certificado_resolveu", "cliente_senha_resolveu"]:
        if "sim" in entrada.lower():
            sessao["etapa"] = "fim"
            return (
                [{"tipo": "texto", "conteudo": "Que otimo! Bom estudo! Qualquer duvida estamos aqui."}],
                sessao
            )
        else:
            sessao["etapa"] = "escalonamento_nome"
            return (
                [
                    {"tipo": "texto", "conteudo": "Sem problema! Vou te conectar com nossa equipe."},
                    {"tipo": "texto", "conteudo": "Qual o seu nome?"}
                ],
                sessao
            )

    # ==================== ESCALONAMENTO HUMANO ====================
    if etapa == "escalonamento_nome":
        dados["nome"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "escalonamento_email"
        return (
            [{"tipo": "texto", "conteudo": "Qual o seu e-mail?"}],
            sessao
        )

    if etapa == "escalonamento_email":
        if "@" not in entrada:
            return (
                [{"tipo": "texto", "conteudo": "Por favor, insira um e-mail valido."}],
                sessao
            )
        dados["email"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "escalonamento_descricao"
        return (
            [{"tipo": "texto", "conteudo": "Descreva brevemente o seu problema:"}],
            sessao
        )

    if etapa == "escalonamento_descricao":
        dados["descricao"] = entrada
        sessao["dados"] = dados
        sessao["etapa"] = "fim"

        print("\n===== CHAMADO DE SUPORTE =====")
        for chave, valor in dados.items():
            print(f"{chave.upper()}: {valor}")
        print("==============================\n")

        return (
            [
                {"tipo": "texto", "conteudo": "Chamado registrado com sucesso!"},
                {"tipo": "texto", "conteudo": "Nossa equipe retornara em ate 1 hora pelo e-mail informado."},
                {"tipo": "texto", "conteudo": "Se preferir, fale conosco pelo WhatsApp: +55 11 95654-9576"}
            ],
            sessao
        )

    # ==================== RAMO OUTRAS DÚVIDAS ====================
    if etapa == "outras_duvidas":
        if "catalogo" in entrada.lower():
            sessao["etapa"] = "outras_satisfeito"
            return (
                [
                    {"tipo": "texto", "conteudo": "Temos mais de 200 cursos nas areas de:"},
                    {"tipo": "texto", "conteudo": "RH, Vendas, Financeiro e Marketing."},
                    {"tipo": "texto", "conteudo": "Isso respondeu sua duvida?"},
                    {"tipo": "botoes", "opcoes": ["Sim, obrigado", "Quero falar com um consultor"]}
                ],
                sessao
            )

        elif "formato" in entrada.lower():
            sessao["etapa"] = "outras_satisfeito"
            return (
                [
                    {"tipo": "texto", "conteudo": "Nossos cursos estao disponiveis em:"},
                    {"tipo": "texto", "conteudo": "Video-aulas, PDFs interativos, Quizzes e com emissao de Certificados."},
                    {"tipo": "texto", "conteudo": "Isso respondeu sua duvida?"},
                    {"tipo": "botoes", "opcoes": ["Sim, obrigado", "Quero falar com um consultor"]}
                ],
                sessao
            )

        elif "valor" in entrada.lower() or "preco" in entrada.lower() or "plano" in entrada.lower():
            sessao["etapa"] = "empresa_nome"
            dados["necessidade"] = "Consulta de valores"
            sessao["dados"] = dados
            return (
                [
                    {"tipo": "texto", "conteudo": "Os valores sao personalizados de acordo com o perfil da empresa."},
                    {"tipo": "texto", "conteudo": "Vou conectar voce com um consultor. Qual o seu nome?"}
                ],
                sessao
            )

        elif "consultor" in entrada.lower() or "falar" in entrada.lower():
            sessao["etapa"] = "empresa_nome"
            dados["necessidade"] = "Falar com consultor"
            sessao["dados"] = dados
            return (
                [
                    {"tipo": "texto", "conteudo": "Com prazer! Vou conectar voce com um consultor."},
                    {"tipo": "texto", "conteudo": "Qual o seu nome?"}
                ],
                sessao
            )

        else:
            return (
                [
                    {"tipo": "texto", "conteudo": "Por favor, escolha uma das opcoes:"},
                    {"tipo": "botoes", "opcoes": [
                        "Catalogo de cursos",
                        "Formatos dos cursos",
                        "Valores e planos",
                        "Falar com um consultor"
                    ]}
                ],
                sessao
            )

    if etapa == "outras_satisfeito":
        if "sim" in entrada.lower() or "obrigado" in entrada.lower():
            sessao["etapa"] = "fim"
            return (
                [{"tipo": "texto", "conteudo": "Fico feliz em ajudar! Qualquer duvida, estamos aqui."}],
                sessao
            )
        else:
            sessao["etapa"] = "empresa_nome"
            dados["necessidade"] = "Falar com consultor"
            sessao["dados"] = dados
            return (
                [{"tipo": "texto", "conteudo": "Certo! Qual o seu nome?"}],
                sessao
            )

    # ==================== FIM ====================
    if etapa == "fim":
        sessao["etapa"] = "inicio"
        sessao["dados"] = {}
        return (
            [
                {"tipo": "texto", "conteudo": "Posso ajudar com mais alguma coisa?"},
                {"tipo": "botoes", "opcoes": [
                    "Sou empresa interessada",
                    "Ja sou cliente ou colaborador",
                    "Outras duvidas"
                ]}
            ],
            sessao
        )

    # Fallback
    sessao["etapa"] = "inicio"
    return (
        [{"tipo": "texto", "conteudo": "Desculpe, nao entendi. Vamos comecar novamente."}],
        sessao
    )
