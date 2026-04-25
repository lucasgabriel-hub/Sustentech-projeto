"""Controla menus e navegação. login, cadastro, sair"""


from pages.auth import menu_login_cadastro
from pages.Dicas import tela_dicas
from pages.metas import tela_metas
from pages.recomendacoes import tela_recomendacoes
from pages.usuarios import tela_usuarios

def menu_principal():
    
    while True:
        print("\nMenu Principal:")
        print("1. Dicas")
        print("2. Metas")
        print("3. Recomendações")
        print("4. Usuários")
        print("5. Sair")

        escolha = input("Digite um número correspondente à opção: ")

        if escolha == '1':
            tela_dicas()
        elif escolha == '2':
            tela_metas()
        elif escolha == '3':
            tela_recomendacoes()
        elif escolha == '4':
            tela_usuarios()
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

if __name__ == "__main__":    menu_login_cadastro()
menu()

