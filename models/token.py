"""
Modelo de domínio: representa tokens de recompensa do usuário.
"""

from dataclasses import dataclass
from datetime import datetime
from models.meta import TipoMeta

# Quantos tokens cada tipo de meta vale ao ser concluída
TOKENS_POR_TIPO: dict[TipoMeta, int] = {
    TipoMeta.DIARIA:  5,
    TipoMeta.SEMANAL: 15,
    TipoMeta.MENSAL:  40,
}

@dataclass
class Token:
    """
    Representa uma transação de tokens no histórico do usuário.
    Cada vez que uma meta é concluída, um registro Token é gerado
    e continuado, formando o histórico completo de recompensas.
    """

    id: int
    usuario_id: int
    meta_id: int
    quantidade: int
    descricao: str
    criado_em: str  #ex.: "2026-05-31 22:00:00 Lucas recebeu 5 tokens por concluir meta diária"

    def __str__(self) -> str:
        return (
            f"🪙 +{self.quantidade} token(s) — {self.descricao} "
            f"({self.criado_em})"
        )
