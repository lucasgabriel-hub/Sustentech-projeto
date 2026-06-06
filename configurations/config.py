"""Arquivo de configurações globais"""
"""
Configurações globais para o projeto, como caminhos de arquivos, chaves de API, etc.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "sustentech.db"

# NewsAPI 
"""
 Obtenha sua chave gratuita em: https://newsapi.org/register
 Substitua "SUA_CHAVE_AQUI" pela sua chave de API.
"""
NEWS_API_KEY = "SUA_CHAVE_AQUI"