"""Autenticação de usuários"""

from database.connection import cadastrar_usuario, conectar_banco
from database.connection import verificar_usuario
from core.menu import menu_principal

def menu_login_cadastro():
    while True:
        print("\n=====Cadastro e Login=====")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        menu_escolhido = input("Digite um número correspondente à opção: ")

        if menu_escolhido == '1':
            login()
            
        elif menu_escolhido == '2':
            cadastro()
            
        elif menu_escolhido == '3':
            exit()
            
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
Controle de autenticação de usuários. Tela de login, cadastro e opção de sair do programa.
"""
def login():
    print("\n=====Login=====")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conexao = conectar_banco()

    usuario = verificar_usuario(conexao, email, senha)
    if usuario:
        menu_principal(usuario)
    else:
        print("Email ou senha incorretos. Tente novamente.")

"""
falta criar a lógica para validar o login, como verificar se o email e senha correspondem a um usuário cadastrado.
"""

def cadastro():
    print("\n=====Cadastro=====")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conexao = conectar_banco()

    cadastrar_usuario(conexao, nome, email, senha)

    print("Cadastro realizado com sucesso! Agora você pode fazer login.")

"""
falta criar a lógica para validar o cadastro, como verificar se o email já está em uso
 e armazenar os dados do usuário de forma segura.
 """
