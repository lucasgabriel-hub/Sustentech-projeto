"""
Modelo de dados para uma notícia ambiental.
"""
 
from dataclasses import dataclass
from typing import Optional
 
 
@dataclass
class Noticia:
    """
    Representa uma notícia retornada pela NewsAPI.
    """
 
    titulo: str
    descricao: Optional[str]
    fonte: str
    url: str
    publicada_em: Optional[str]
 
    def resumo(self) -> str:
        """
        Retorna um resumo formatado da notícia.
        """
        desc = self.descricao or "Sem descrição disponível."
        # Limita a descrição a 200 caracteres para exibição no terminal
        if len(desc) > 200:
            desc = desc[:197] + "..."
        return desc
 
    def data_formatada(self) -> str:
        """
        Retorna a data de publicação formatada (somente data, sem horário).
        """
        if not self.publicada_em:
            return "Data desconhecida"
        # A NewsAPI retorna o formato '2024-06-05T14:30:00Z'
        return self.publicada_em[:10]
 