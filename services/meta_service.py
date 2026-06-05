"""Serviço de metas sustentáveis."""

from database.repositories import MetaRepository
from models.meta import Meta, TipoMeta, StatusMeta
from services.token_service import TokenService


class MetaService:
    """
    Gerencia as metas sustentáveis dos usuários, incluindo listagem e conclusão.
    """
    def __init__(self, conexao) -> None:
        self._repo = MetaRepository(conexao)
        self._token_service = TokenService(conexao)

    def listar(self, usuario_id: int, tipo: TipoMeta) -> list[Meta]:
        return self._repo.listar_por_tipo(usuario_id, tipo.value)

    def concluir(self, meta: Meta, usuario_id: int) -> tuple[bool, str, int]:
        """
        Tenta concluir uma meta e concede tokens como recompensa.
        Retorna (sucesso, mensagem, tokens_ganhos).
        """
        try:
            meta.concluir()                              
            self._repo.concluir(meta.id, usuario_id)    

            tokens = self._token_service.conceder(meta)  
            mensagem = (
                f"🎉 Parabéns! Meta concluída! Você ganhou {tokens} token(s)! 🪙"
            )
            return True, mensagem, tokens
        except ValueError as e:
            return False, f"⚠️ {e}", 0
