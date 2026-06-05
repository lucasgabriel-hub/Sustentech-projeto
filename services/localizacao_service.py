"""
Módulo responsável por lidar com a localização geográfica, incluindo a obtenção de coordenadas
a partir de um endereço e a busca por ecopontos próximos usando a API do OpenStreetMap.
"""

import requests
from models.mapa import PontoDescarte


class LocalizacaoService:

    HEADERS = {
        "User-Agent": "SustenTech"
    }
    
    @staticmethod
    def obter_coordenadas(local: str):
        """
        Obtém as coordenadas (latitude e longitude) de um endereço usando a API do Nominatim.
        Retorna uma tupla (latitude, longitude) ou None se o endereço não for encontrado.
        """

        resposta = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q": local,
                "format": "json",
                "limit": 1
            },
            headers=LocalizacaoService.HEADERS,
            timeout=10
        )

        dados = resposta.json()

        if not dados:
            return None

        return (
            float(dados[0]["lat"]),
            float(dados[0]["lon"])
        )

    @staticmethod
    def buscar_ecopontos(
        latitude: float,
        longitude: float
    ) -> list[PontoDescarte]:
        """
        Busca ecopontos próximos a uma localização usando a API do Overpass do OpenStreetMap.
        Retornando uma lista de objetos PontoDescarte contendo o nome e as coordenadas de cada ecoponto encontrado.
        """

        consulta = f"""
        [out:json][timeout:25];
        (
          node["amenity"="recycling"](around:10000,{latitude},{longitude});
          way["amenity"="recycling"](around:10000,{latitude},{longitude});
          relation["amenity"="recycling"](around:10000,{latitude},{longitude});
        );
        out center;
        """

        resposta = requests.get(
            "https://overpass-api.de/api/interpreter",
            params={"data": consulta},
            headers=LocalizacaoService.HEADERS,
            timeout=30
        )

        dados = resposta.json()

        elementos = dados.get("elements", [])

        pontos = []

        for item in elementos:

            tags = item.get("tags", {})

            nome = (
                tags.get("name")
                or tags.get("operator")
                or tags.get("brand")
                or tags.get("description")
                or tags.get("addr:street")
                or "Ecoponto sem identificação"
            )

            lat = item.get(
                "lat",
                item.get("center", {}).get("lat")
            )

            lon = item.get(
                "lon",
                item.get("center", {}).get("lon")
            )

            if lat is None or lon is None:
                continue

            pontos.append(
                PontoDescarte(
                    nome=nome,
                    latitude=float(lat),
                    longitude=float(lon)
                )
            )

        return pontos
    
    @staticmethod
    def obter_endereco(latitude: float, longitude: float) -> str:
        """
        Obtém o endereço completo a partir de coordenadas usando a API do Nominatim.
        Retorna uma string com o endereço ou uma mensagem de erro caso não seja possível obter o endereço.
        """

        resposta = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={
                "lat": latitude,
                "lon": longitude,
                "format": "json"
            },
            headers=LocalizacaoService.HEADERS,
            timeout=10
        )

        dados = resposta.json()

        return dados.get(
            "display_name",
            "Endereço não encontrado"
        )
    