"""Serviço de gerenciamento de usuários."""

from database.repositories import UsuarioRepository
from models.usuario import Usuario


class UsuarioService:
    """
    Serviço para operações relacionadas a usuários.
    Responsável por validar dados e interagir com o repositório de usuários.
    """
    def __init__(self, conexao) -> None:
        self._repo = UsuarioRepository(conexao)

    def atualizar(self, usuario_id: int, nome: str, email: str, senha: str) -> tuple[bool, list[str]]:
        """
        Atualiza os dados de um usuário existente.
        Retorna uma tupla indicando sucesso e uma lista de mensagens de erro, se houver.
        """
        erros: list[str] = []
        if not Usuario.validar_nome(nome):
            erros.append("Nome deve ter entre 3 e 20 caracteres.")
        if not Usuario.validar_email(email):
            erros.append("Email deve terminar com @gmail.com.")
        if not Usuario.validar_senha(senha):
            erros.append("Senha deve ter pelo menos 6 caracteres.")

        if erros:
            return False, erros

        self._repo.atualizar(usuario_id, nome, email, senha)
        return True, []

    def listar(self) -> list[Usuario]:
        """
        Retorna uma lista de todos os usuários cadastrados.
        """
        return self._repo.listar_todos()

    def deletar(self, usuario_id: int) -> None:
        """
        Deleta um usuário pelo seu ID.
        """
        self._repo.deletar(usuario_id)
