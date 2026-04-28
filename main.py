"""Iniciar o programa, Chamar o menu principal e Controlar o fluxo geral"""

from database.connection import conectar_banco
from database.connection import criar_tabela_usuarios
from core.menu import menu_principal
from pages.auth import menu_login_cadastro
from database.connection import conectar_banco
from database.connection import criar_tabela_metas
from pages.metas import tela_metas
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))


"""
Função para iniciar o banco de dados, criando a tabela de usuários caso ela ainda não exista.
"""

def iniciar_banco():

    conexao = conectar_banco()

    criar_tabela_usuarios(conexao)
    criar_tabela_metas(conexao)

    conexao.close()


"""
função principal do programa, responsável por iniciar o banco de dados e chamar o menu de login/cadastro.
"""

def main():
    iniciar_banco()

    usuario = menu_login_cadastro()
    if usuario:
        menu_principal(usuario)

if __name__ == "__main__":
    main()


