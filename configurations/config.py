"""Arquivo de configurações globais"""
"""
Configurações globais para o projeto, como caminhos de arquivos, chaves de API, etc.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "sustentech.db"