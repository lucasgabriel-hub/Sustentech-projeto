"""
Serviço de notícias ambientais usando a NewsAPI.
 
Documentação da NewsAPI: https://newsapi.org/docs
Para obter uma chave gratuita: https://newsapi.org/register
 
Configuração:
    Defina a variável NEWS_API_KEY em configurations/config.py com sua chave.
"""
 
import urllib.request
import urllib.parse
import json
from typing import Optional
 
from models.noticia import Noticia
 
 
# Constantes 
 
_BASE_URL = "https://newsapi.org/v2/everything"
 
# Termos de busca em português e inglês para cobrir mais resultados
_QUERY_PADRAO = (
    "meio ambiente OR sustentabilidade OR reciclagem OR "
    "mudanças climáticas OR desmatamento OR energia renovável"
)
 
_PAGE_SIZE_PADRAO = 10  
 
 
# Serviço
 
class NoticiasService:
    """
    Responsável por buscar notícias ambientais na NewsAPI.
    Args:
        api_key: Chave de acesso à NewsAPI. Se não fornecida, tenta ler de
                 configurations/config.py (variável NEWS_API_KEY).
    """
 
    def __init__(self, api_key: Optional[str] = None) -> None:
        if api_key:
            self._api_key = api_key
        else:
            # Importação local para evitar dependência circular no topo do módulo
            try:
                from configurations.config import NEWS_API_KEY
                self._api_key = NEWS_API_KEY
            except (ImportError, AttributeError):
                self._api_key = ""
 
    # Público 
 
    def buscar_noticias(
        self,
        query: str = _QUERY_PADRAO,
        quantidade: int = _PAGE_SIZE_PADRAO,
        idioma: str = "pt",
    ) -> tuple[list[Noticia], Optional[str]]:
        """
        Busca as notícias mais recentes com base na query informada.
 
        Returns:
            (lista_de_noticias, mensagem_de_erro)
            Em caso de sucesso, mensagem_de_erro será None.
            Em caso de falha, lista_de_noticias será vazia.
        """
        if not self._api_key or self._api_key == "SUA_CHAVE_AQUI":
            return [], (
                "Chave da NewsAPI não configurada.\n"
                "Acesse https://newsapi.org/register para obter uma chave gratuita\n"
                "e adicione-a em configurations/config.py como NEWS_API_KEY."
            )
 
        params = {
            "q": query,
            "language": idioma,
            "sortBy": "publishedAt",
            "pageSize": min(quantidade, 100),
            "apiKey": self._api_key,
        }
 
        url = f"{_BASE_URL}?{urllib.parse.urlencode(params)}"
 
        try:
            with urllib.request.urlopen(url, timeout=10) as resposta:
                dados = json.loads(resposta.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            corpo = e.read().decode("utf-8") if e.fp else ""
            try:
                mensagem_api = json.loads(corpo).get("message", "")
            except json.JSONDecodeError:
                mensagem_api = corpo
            return [], f"Erro HTTP {e.code}: {mensagem_api or e.reason}"
        except urllib.error.URLError as e:
            return [], f"Erro de conexão: {e.reason}. Verifique sua internet."
        except Exception as e:
            return [], f"Erro inesperado: {e}"
 
        if dados.get("status") != "ok":
            return [], dados.get("message", "Resposta inesperada da NewsAPI.")
 
        artigos = dados.get("articles", [])
        if not artigos:
            return [], "Nenhuma notícia encontrada para os termos buscados."
 
        noticias = [self._converter_artigo(a) for a in artigos]
        return noticias, None
 
    # Privado
 
    @staticmethod
    def _converter_artigo(artigo: dict) -> Noticia:
        """Converte um dicionário de artigo da API em um objeto Noticia."""
        fonte = artigo.get("source", {}) or {}
        return Noticia(
            titulo=artigo.get("title") or "Título não disponível",
            descricao=artigo.get("description"),
            fonte=fonte.get("name") or "Fonte desconhecida",
            url=artigo.get("url") or "",
            publicada_em=artigo.get("publishedAt"),
        )
 