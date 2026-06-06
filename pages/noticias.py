"""
Tela de notícias ambientais — integração com a NewsAPI.
"""
 
from services.noticias_service import NoticiasService
from models.noticia import Noticia
from utils.utilidades import UI
 
 
# Configuração de exibição 
 
_QUANTIDADE_NOTICIAS = 10   
 
 
# Tela principal 
 
def tela_noticias() -> None:
    """
    Exibe as últimas notícias ambientais obtidas da NewsAPI.
    O usuário pode navegar pela lista e abrir o link de qualquer notícia.
    """
    service = NoticiasService()
 
    while True:
        UI.cabecalho("📰 Notícias Ambientais")
        print("1. Carregar últimas notícias (padrão)")
        print("2. Buscar por palavra-chave")
        print("3. Voltar ao menu principal")
        UI.separador()
 
        opcao = input("Escolha: ").strip()
 
        if opcao == "1":
            UI.limpar()
            _exibir_noticias(service, query=None)
 
        elif opcao == "2":
            UI.separador()
            termo = input("Digite o termo de busca: ").strip()
            if not termo:
                UI.erro("Termo de busca vazio.")
                UI.pausar()
                UI.limpar()
                continue
            UI.limpar()
            _exibir_noticias(service, query=termo)
 
        elif opcao == "3":
            break
 
        else:
            UI.erro("Opção inválida.")
            UI.pausar()
            UI.limpar()
 
 
# Funções auxiliares 
 
def _exibir_noticias(service: NoticiasService, query: str | None) -> None:
    """
    Carrega e exibe a lista de notícias. Permite ao usuário selecionar
    uma notícia para ver os detalhes completos.
    """
    print("🔎 Buscando notícias... aguarde.\n")
 
    kwargs: dict = {"quantidade": _QUANTIDADE_NOTICIAS}
    if query:
        kwargs["query"] = query
 
    noticias, erro = service.buscar_noticias(**kwargs)
 
    if erro:
        UI.erro(erro)
        UI.pausar()
        UI.limpar()
        return
 
    while True:
        UI.cabecalho(f"📰 Últimas Notícias — {len(noticias)} resultados")
 
        for i, noticia in enumerate(noticias, start=1):
            print(f"{i:2}. [{noticia.data_formatada()}] {noticia.titulo}")
            print(f"     Fonte: {noticia.fonte}")
            UI.separador()
 
        print(f"Digite o número da notícia para ver detalhes (1-{len(noticias)})")
        print("0. Voltar")
        UI.separador()
 
        escolha = input("Escolha: ").strip()
 
        if escolha == "0":
            UI.limpar()
            break
 
        if escolha.isdigit() and 1 <= int(escolha) <= len(noticias):
            UI.limpar()
            _exibir_detalhe(noticias[int(escolha) - 1])
        else:
            UI.erro("Número inválido.")
            UI.pausar()
            UI.limpar()
 
 
def _exibir_detalhe(noticia: Noticia) -> None:
    """
    Exibe os detalhes completos de uma notícia selecionada.
    """
    UI.cabecalho("📄 Detalhe da Notícia")
    print(f"Título  : {noticia.titulo}")
    print(f"Fonte   : {noticia.fonte}")
    print(f"Data    : {noticia.data_formatada()}")
    UI.separador()
    print("Descrição:")
    print(noticia.resumo())
    UI.separador()
    print(f"Leia mais: {noticia.url}")
    UI.separador()
    UI.pausar("Pressione Enter para voltar à lista...")
    UI.limpar()
 