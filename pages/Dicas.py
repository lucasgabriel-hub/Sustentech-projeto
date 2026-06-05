"""Tela de dicas sustentáveis."""

from utils.utilidades import UI

"""
Dicas para prolongar a vida útil dos aparelhos, manutenção, reutilização e descarte consciente.
"""

_DICAS: dict[str, tuple[str, str]] = {
    "1": (
        "Vida Útil de Aparelhos",
        """
📱 Smartphones
  • Evite deixar a bateria chegar a 0% ou ficar sempre em 100%.
  • Use capinha e película para evitar danos físicos.
  • Reduza o brilho da tela para economizar bateria.

📺 TVs
  • Desligue da tomada quando não estiver em uso por longos períodos.
  • Evite exposição direta ao sol.
  • Limpe a tela com pano adequado (sem produtos agressivos).

💻 Computadores/Notebooks
  • Evite superaquecimento (use em superfícies planas).
  • Faça limpezas periódicas (poeira interna).
  • Atualize o sistema para manter o desempenho.

🔊 Caixas de som
  • Não use no volume máximo por muito tempo.
  • Proteja contra umidade.

🎧 Fones de ouvido
  • Evite enrolar o fio com força.
  • Limpe regularmente (especialmente intra-auriculares).
  • Guarde em estojos para evitar danos.
""",
    ),
    "2": (
        "Manutenção e Cuidados",
        """
  • Faça limpezas regulares para evitar acúmulo de poeira.
  • Use carregadores originais ou certificados.
  • Evite quedas e impactos.
  • Não exponha aparelhos à água ou calor excessivo.
  • Atualize softwares e antivírus regularmente.
""",
    ),
    "3": (
        "Reutilização e Reaproveitamento",
        """
  • Transforme celulares antigos em câmeras de segurança ou despertadores.
  • Use notebooks antigos para estudos básicos ou servidores simples.
  • Aproveite peças (cabos, carregadores, HDs).
  • Doe aparelhos que ainda funcionam.
  • Reutilize caixas e embalagens para organização.
""",
    ),
    "4": (
        "Descarte e Consumo Consciente",
        """
  • Nunca jogue eletrônicos no lixo comum (contêm materiais tóxicos).
  • Procure pontos de coleta de lixo eletrônico na sua cidade.
  • Prefira marcas com compromisso ambiental.
  • Evite comprar por impulso — só adquira o necessário.
  • Dê preferência a produtos duráveis e com garantia maior.
""",
    ),
}


def tela_dicas() -> None:
    """
    Exibe dicas sustentáveis para prolongar a vida útil dos aparelhos, manutenção, reutilização e descarte consciente.
    O usuário pode escolher entre diferentes categorias de dicas e visualizar o conteúdo correspondente.
    """
    while True:
        UI.cabecalho("Dicas Sustentáveis 🌱")
        for chave, (titulo, _) in _DICAS.items():
            print(f"{chave}. {titulo}")
        print("5. Voltar ao menu principal")
        UI.separador()

        opcao = input("Escolha: ").strip()

        if opcao in _DICAS:
            UI.limpar()
            titulo, conteudo = _DICAS[opcao]
            print(f"{'='*9} {titulo} {'='*9}")
            print(conteudo)
            UI.pausar("Pressione Enter para voltar às dicas...")
            UI.limpar()

        elif opcao == "5":
            break

        else:
            UI.erro("Opção inválida.")
            UI.pausar()
            UI.limpar()
