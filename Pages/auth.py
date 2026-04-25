"""Autenticação de usuários"""

def menu_login_cadastro():
    while True:
        print("\n=====Cadastro e Login=====")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        menu_escolhido = input("Digite um número correspondente à opção: ")

        if menu_escolhido == '1':
            
            
        elif menu_escolhido == '2':
            print("Tela de Cadastro ")
            
        elif menu_escolhido == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
Controle de autenticação de usuários. Tela de login, cadastro e opção de sair do programa.
"""
def login():
    print("\n=====Login=====")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    print("Login realizado com sucesso! Bem-vindo(a)!")

"""
falta criar a lógica para validar o login, como verificar se o email e senha correspondem a um usuário cadastrado.
"""

def cadastro():
    print("\n=====Cadastro=====")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    print("Cadastro realizado com sucesso! Agora você pode fazer login.")

"""
falta criar a lógica para validar o cadastro, como verificar se o email já está em uso
 e armazenar os dados do usuário de forma segura.
 """
