"""
Rotas de descarte utilizando a API da OpenStreetMap.
"""

from utils.utilidades import UI
from services.localizacao_service import LocalizacaoService

"""
Função para exibir as rotas de descarte próximas ao usuário.
Utiliza a API da OpenStreetMap para buscar ecopontos próximos às coordenadas do usuário
"""
def rotas_descarte() -> None:

    UI.cabecalho("Rotas de Descarte ♻️")

    local = input(
        "Digite sua cidade ou endereço: "
    ).strip()

    coordenadas = (
        LocalizacaoService
        .obter_coordenadas(local)
    )

    if coordenadas is None:
        UI.erro(
            "Não foi possível localizar o endereço."
        )
        UI.pausar()
        return

    latitude, longitude = coordenadas

    print("Buscando ecopontos próximos...")

    try:

        pontos = (
            LocalizacaoService
            .buscar_ecopontos(
                latitude,
                longitude
            )
        )

    except Exception as erro:

        UI.erro(
            f"Erro ao consultar OpenStreetMap: {erro}"
        )

        UI.pausar()
        return

    UI.separador()

    print(
        "Ecopontos encontrados "
        "(raio de 10 km)"
    )

    UI.separador()

    if not pontos:

        print(
            "Nenhum ecoponto encontrado "
            "na região."
        )

        UI.pausar()
        return

    for indice, ponto in enumerate(
        pontos,
        start=1
    ):

        endereco = (
            LocalizacaoService
            .obter_endereco(
                ponto.latitude,
                ponto.longitude
            )
        )

        nome_exibicao = (
            "Ecoponto"
            if ponto.nome == "Ecoponto sem identificação"
            else ponto.nome
        )

        print(
            f"{indice}. {nome_exibicao}"
        )

        print(
            f"   Endereço: {endereco}"
        )

        print("-" * 40)

    UI.pausar()
    UI.limpar()