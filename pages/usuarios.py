"""Tela de gerenciamento de usuários."""

from services.usuario_service import UsuarioService
from models.usuario import Usuario
from utils.utilidades import UI


def tela_usuarios(conexao, usuario_id: int) -> bool:
    """
    Retorna True se a conta foi deletada (forçando logout),
    False caso contrário.
    """
    service = UsuarioService(conexao)

    UI.cabecalho("👥 Gerenciamento de Usuários")
    print("1. Atualizar dados pessoais")
    print("2. Listar usuários cadastrados")
    print("3. Deletar minha conta")
    print("4. Voltar ao menu principal")
    UI.separador()

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        UI.limpar()
        return _atualizar(service, usuario_id)

    elif opcao == "2":
        UI.limpar()
        _listar(service)

    elif opcao == "3":
        UI.limpar()
        return _deletar(service, usuario_id)

    elif opcao == "4":
        UI.limpar()

    return False


def _atualizar(service: UsuarioService, usuario_id: int) -> bool:
    """
    Permite ao usuário atualizar seus dados pessoais.
    Retorna False, pois atualizar não força logout.
    """
    UI.cabecalho("Atualizar Dados Pessoais")
    nome  = input("Novo nome: ").strip()
    email = input("Novo email: ").strip()
    senha = input("Nova senha: ").strip()

    sucesso, erros = service.atualizar(usuario_id, nome, email, senha)
    if sucesso:
        UI.sucesso("Dados atualizados com sucesso!")
    else:
        for erro in erros:
            UI.erro(erro)

    UI.pausar()
    UI.limpar()
    return False


def _listar(service: UsuarioService) -> None:
    UI.cabecalho("Usuários Cadastrados")
    for u in service.listar():
        print(f"  ID: {u.id} | {u.nome} | {u.email}")
    UI.pausar()
    UI.limpar()


def _deletar(service: UsuarioService, usuario_id: int) -> bool:
    """
    Permite ao usuário deletar sua conta.
    Retorna True se a conta for deletada, False caso contrário.
    """
    if UI.confirmar("Tem certeza que deseja deletar sua conta?"):
        service.deletar(usuario_id)
        UI.sucesso("Conta deletada.")
        return True  # sinaliza logout ao menu principal.

    UI.erro("Operação cancelada.")
    UI.pausar()
    UI.limpar()
    return False
