"""
Modelo para representar um ponto de descarte de resíduos.
"""

class PontoDescarte:
    """
    Classe que representa um ponto de descarte de resíduos.
    """
    def __init__(
        self,
        nome: str,
        latitude: float,
        longitude: float
    ):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude