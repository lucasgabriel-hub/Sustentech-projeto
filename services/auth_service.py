"""Serviço de autenticação — orquestra login e cadastro."""

from typing import Optional

from database.repositories import UsuarioRepository, MetaRepository
from models.usuario import Usuario, UsuarioCadastro
from utils.utilidades import UI


class AuthService:
    """
    Contém a lógica de negócio de autenticação.
    Separar da UI permite testar as regras sem simular input do terminal.
    """

    def __init__(self, conexao) -> None:
        self._usuario_repo = UsuarioRepository(conexao)
        self._meta_repo = MetaRepository(conexao)

    def login(self, email: str, senha: str) -> Optional[Usuario]:
        """
        Retorna o Usuario autenticado ou None.
        """
        return self._usuario_repo.buscar_por_credenciais(email, senha)

    def cadastrar(self, dto: UsuarioCadastro) -> tuple[bool, list[str], Optional[int]]:
        """
        se tentar cadastrar um novo usuário.
        Retorna no terminal. (sucesso, erros, usuario_id).
        """
        valido, erros = dto.is_valido()
        if not valido:
            return False, erros, None

        usuario_id = self._usuario_repo.cadastrar(dto)
        if usuario_id is None:
            return False, ["Este email já está em uso, tente de novo."], None

        self._meta_repo.inserir_metas_padrao(usuario_id)
        return True, [], usuario_id
