"""
Serviço de tokens — recompensas por metas concluídas.
"""

from database.repositories import TokenRepository
from models.meta import Meta, TipoMeta
from models.token import TOKENS_POR_TIPO, Token


class TokenService:
    """
    Encapsula as regras de negócio dos tokens.
    - Conceder tokens ao concluir uma meta
    - Consultar saldo atual
    - Exibir histórico de recompensas
    """

    def __init__(self, conexao) -> None:
        self._repo = TokenRepository(conexao)

    """
    Regras de negócio:
    - Cada tipo de meta tem um valor fixo de tokens
    """

    def tokens_da_meta(self, tipo: TipoMeta) -> int:
        """
        Retorna quantos tokens uma meta daquele tipo vale.
        """
        return TOKENS_POR_TIPO.get(tipo, 0)

    def conceder(self, meta: Meta) -> int:
        """
        Registra a recompensa ao concluir uma meta.
        Retorna a quantidade de tokens concedidos.
        """
        quantidade = self.tokens_da_meta(meta.tipo)
        if quantidade <= 0:
            return 0

        descricao = f"Meta concluída: {meta.descricao}"
        self._repo.registrar(meta.usuario_id, meta.id, quantidade, descricao)
        return quantidade

    def saldo(self, usuario_id: int) -> int:
        """
        Retorna o total de tokens acumulados pelo usuário.
        """
        return self._repo.saldo(usuario_id)

    def historico(self, usuario_id: int, limite: int = 10) -> list[Token]:
        """
        Retorna os últimos registros de tokens do usuário.
        """
        return self._repo.historico(usuario_id, limite)
