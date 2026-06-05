"""Telas de autenticação: login, cadastro e boas-vindas."""

from models.usuario import Usuario, UsuarioCadastro
from services.auth_service import AuthService
from utils.utilidades import UI


def menu_login_cadastro(conexao) -> Usuario:
    """
    Loop principal de autenticação. Retorna o Usuario logado.
    """
    service = AuthService(conexao)

    while True:
        UI.cabecalho("♻️  Bem-vindo ao Sustentech!  ♻️")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")
        UI.separador()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            UI.limpar()
            usuario = _tela_login(service)
            if usuario:
                return usuario

        elif opcao == "2":
            UI.limpar()
            _tela_cadastro(service)

        elif opcao == "3":
            print("Até logo! 🌱")
            exit()

        else:
            UI.erro("Opção inválida. Tente novamente.")
            UI.limpar()


def _tela_login(service: AuthService):
    """
    Tela de login. Retorna o Usuario se o login for bem-sucedido, ou None caso contrário.
    """
    UI.cabecalho("Login")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    UI.separador()

    usuario = service.login(email, senha)
    if usuario:
        UI.limpar()
        return usuario

    UI.erro("Email ou senha incorretos.")
    UI.pausar()
    UI.limpar()
    return None


def _tela_cadastro(service: AuthService) -> None:
    """
    Tela de cadastro. Não retorna nada, apenas exibe mensagens de sucesso ou erro.
    """
    UI.cabecalho("Cadastro")

    nome  = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    UI.separador()

    dto = UsuarioCadastro(nome=nome, email=email, senha=senha)
    sucesso, erros, _ = service.cadastrar(dto)

    if sucesso:
        UI.sucesso("Cadastro realizado! Faça login para continuar.")
    else:
        for erro in erros:
            UI.erro(erro)

    UI.pausar()
    UI.limpar()
