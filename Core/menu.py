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

        funçao_escolhida = input("Digite um número correspondente à opção: ")

        if funçao_escolhida == '1':
            tela_dicas()
        elif funçao_escolhida == '2':
            tela_metas()
        elif funçao_escolhida == '3':
            tela_recomendacoes()
        elif funçao_escolhida == '4':
            tela_usuarios()
        elif funçao_escolhida == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

if __name__ == "__main__":    menu_login_cadastro()
menu()


