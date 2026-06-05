"""
Ponto de entrada da aplicação Sustentech.
"""

from database.connection import conectar_banco, inicializar_banco
from pages.auth import menu_login_cadastro
from pages.menu import menu_principal

def main() -> None:
    conexao = conectar_banco()
    inicializar_banco(conexao)

    # Loop externo: permite que o usuário faça logout e entre com outra conta
    while True:
        usuario = menu_login_cadastro(conexao)
        menu_principal(conexao, usuario)

if __name__ == "__main__":
    main()
