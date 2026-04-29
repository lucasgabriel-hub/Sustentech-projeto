"""Autenticação de usuários"""

from utils.utilidades import limpar_tela, tamanho   
from database.connection import cadastrar_usuario, conectar_banco, verificar_usuario
from database.connection import inserir_metas_padrao

def menu_login_cadastro(conexao):
    while True:
        print("="*40)
        print('​♻️ Bem-vindo ao Sustentech!​♻️')
        print("="*40)
        print('1. Login')
        print('2. Cadastro')
        print('3. Sair')

        menu_escolhido = input('Digite um número correspondente à opção: ')

        if menu_escolhido == '1':
            limpar_tela()
            usuário = login(conexao)
            if usuário:
                return usuário
            
        elif menu_escolhido == '2':
            limpar_tela()
            cadastro(conexao)
            
        elif menu_escolhido == '3':
            exit()
            
        else:
            print('​❌Opção inválida. Por favor, escolha uma das opções acima.')
            limpar_tela()
    
    

"""
Controle de autenticação de usuários. Tela de login, cadastro e opção de sair do programa.
"""
def login(conexao):
    print("="*40)
    print('Login')
    print("="*40)
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    print("-"*40)

    usuario = verificar_usuario(conexao, email, senha)

    if usuario:
        limpar_tela()
        return {"id": usuario[0],
                "nome": usuario[1],
                "email": usuario[2]}
    else:
        print('​❌ Email ou senha incorretos. Tente novamente.')
        input('Pressione Enter para continuar...')
        limpar_tela()
        return None

"""
falta criar a lógica para validar o login, como verificar se o email e senha correspondem a um usuário cadastrado.
"""

def cadastro(conexao):
    print("="*40)
    print('Cadastro')
    print("="*40)
    while True:
        nome = input('Digite seu nome: ')
        if tamanho(nome):
            break
        print("Tamanho do nome inválido. Tente Novamente.")

    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    print("-"*40)

    if not email.endswith('@gmail.com'):
        print('❌ Só é permitido email que termine com @gmail.com')
        input('Pressione Enter para continuar...')  
        limpar_tela()  
        return

    conexao = conectar_banco()

    usuario_id = cadastrar_usuario(conexao, nome, email, senha)
    if usuario_id:
        inserir_metas_padrao(conexao, usuario_id)

    conexao.close()