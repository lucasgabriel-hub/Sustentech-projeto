"""Iniciar o programa, Chamar o menu principal e Controlar o fluxo geral"""

from database.connection import conectar_banco
from pages.auth import menu_login_cadastro
from database.connection import criar_tabela_usuarios
from core.menu import menu_principal

"""
Função para iniciar o banco de dados, criando a tabela de usuários caso ela ainda não exista.
"""

def iniciar_banco():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    criar_tabela_usuarios(conexao)

    cursor.close()
    conexao.close()


"""
função principal do programa, responsável por iniciar o banco de dados e chamar o menu de login/cadastro.
"""

def main():
    usuario = menu_login_cadastro()
    if usuario:
        menu_principal(usuario)

"""
O programa inicia chamando a função main(), que por sua vez chama o menu de login/cadastro.
 Após um login bem-sucedido, o menu principal é exibido.
"""

if __name__ == "__main__":
    main()


