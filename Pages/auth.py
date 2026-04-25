"""Autenticação de usuários"""

def menu_login_cadastro():
    while True:
        print("\n=====Cadastro e Login=====")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        escolha = input("Digite um número correspondente à opção: ")

        if escolha == '1':
            print("Tela de Login ")
            
        elif escolha == '2':
            print("Tela de Cadastro ")
            
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
Controle de autenticação de usuários. Tela de login, cadastro e opção de sair do programa.
"""
