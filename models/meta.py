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