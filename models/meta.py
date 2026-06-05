"""
Modelo de domínio: representa uma Meta sustentável.
"""

from dataclasses import dataclass
from enum import Enum

class TipoMeta(str, Enum):
    """
    Garante que só tipos válidos sejam usados no sistema.
    """
    DIARIA = "diaria"
    SEMANAL = "semanal"
    MENSAL = "mensal"

class StatusMeta(str, Enum):
    """
    Garante que só status válidos sejam usados no sistema.
    """
    PENDENTE = "pendente"
    CONCLUIDA = "concluída"

@dataclass
class Meta:
    """
    Representa uma meta sustentável de um usuário.
    """

    id: int
    usuario_id: int
    tipo: TipoMeta
    descricao: str
    status: StatusMeta

    
    # Comportamentos
    
    @property
    def esta_concluida(self) -> bool:
        return self.status == StatusMeta.CONCLUIDA

    def concluir(self) -> None:
        """Transiciona o status para concluída (regra de negócio isolada)."""
        if self.esta_concluida:
            raise ValueError("Meta já foi concluída anteriormente.")
        self.status = StatusMeta.CONCLUIDA

    def icone_status(self) -> str:
        return "✅" if self.esta_concluida else "⏳"

    def __str__(self) -> str:
        return (
            f"{self.icone_status()} [{self.tipo.value.upper()}] "
            f"{self.descricao} — {self.status.value}"
        )

    # Fábrica de metas padrão
    
    @staticmethod
    def metas_padrao(usuario_id: int) -> list["Meta"]:
        """
        Retorna as metas padrão que todo novo usuário recebe.
        Centralizar aqui evita duplicação entre connection.py e outros lugares.
        """
        dados = [
            (TipoMeta.DIARIA,  "Desligar luzes ao sair dos ambientes"),
            (TipoMeta.DIARIA,  "Reduzir tempo de banho"),
            (TipoMeta.DIARIA,  "Evitar standby"),
            (TipoMeta.SEMANAL, "Separar lixo reciclável"),
            (TipoMeta.SEMANAL, "Evitar plástico descartável"),
            (TipoMeta.SEMANAL, "Usar transporte alternativo"),
            (TipoMeta.MENSAL,  "Reduzir consumo de energia"),
            (TipoMeta.MENSAL,  "Doar ou reutilizar objetos"),
            (TipoMeta.MENSAL,  "Aprender prática sustentável"),
        ]
        return [
            Meta(id=0, usuario_id=usuario_id, tipo=t, descricao=d,
                 status=StatusMeta.PENDENTE)
            for t, d in dados
        ]
