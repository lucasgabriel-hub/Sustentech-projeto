"""Autenticação de usuários"""

from database.connection import cadastrar_usuario, conectar_banco, verificar_usuario
from database.connection import inserir_metas_padrao

def menu_login_cadastro():
    while True:
        print("\n=====Cadastro e Login=====")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        menu_escolhido = input("Digite um número correspondente à opção: ")

        if menu_escolhido == '1':
            usuário = login()
            if usuário:
                return usuário
            
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
    conexao.close()

    if usuario:
        return {"id": usuario[0],
                "nome": usuario[1],
                "email": usuario[2]}
    else:
        print("Email ou senha incorretos. Tente novamente.")
        return None

"""
falta criar a lógica para validar o login, como verificar se o email e senha correspondem a um usuário cadastrado.
"""

def cadastro():
    print("\n=====Cadastro=====")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if not email.endswith("@gmail.com"):
        print("❌ Só é permitido email que termine com @gmail.com")
        return

    conexao = conectar_banco()

    usuario_id = cadastrar_usuario(conexao, nome, email, senha)
    if usuario_id:
        inserir_metas_padrao(conexao, usuario_id)
        print('cadastro realizado com sucesso!')

    conexao.close()