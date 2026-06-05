"""Gerencia a conexão com o SQLite e inicializa o banco."""

import sqlite3
from configurations.config import DB_PATH
from database.repositories import UsuarioRepository, MetaRepository, TokenRepository

"""
Este módulo é responsável por estabelecer a conexão com o banco de dados 
SQLite e garantir que as tabelas necessárias sejam criadas. 
"""
def conectar_banco() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def inicializar_banco(conexao: sqlite3.Connection) -> None:
    """
    Cria todas as tabelas necessárias, se ainda não existirem.
    Chamado uma vez na inicialização do programa (main.py).
    """
    UsuarioRepository(conexao).criar_tabela()
    MetaRepository(conexao).criar_tabela()
    TokenRepository(conexao).criar_tabela()