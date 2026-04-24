"""Controla menus e navegação. login, cadastro, sair"""
from Pages.auth import tela_auth
from Pages.Dicas import tela_dicas
from Pages.metas import tela_metas
from Pages.recomendacoes import tela_recomendacoes
from Pages.usuarios import tela_usuarios

def menu():
    """Menu principal do programa, onde o usuário pode escolher entre as opções disponíveis."""
    while True:
        print("\nMenu Principal:")
        print("1. Dicas")
        print("2. Metas")
        print("3. Recomendações")
        print("4. Usuários")
        print("5. Sair")

        choice = input("Digite um número correspondente à opção: ")

        if choice == '1':
            tela_dicas()
        elif choice == '2':
            tela_metas()
        elif choice == '3':
            tela_recomendacoes()
        elif choice == '4':
            tela_usuarios()
        elif choice == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

if __name__ == "__main__":    tela_auth()
menu()

