"""Controla menus e navegação. login, cadastro, sair"""

from pages.Dicas import tela_dicas
from pages.metas import tela_metas
from pages.recomendacoes import tela_recomendacoes
from pages.usuarios import tela_usuarios
from database.connection import conectar_banco

def menu_principal(usuario):
    usuario_id = usuario["id"]
    conexao = conectar_banco()
    
    while True:
        print("\n=====Menu Principal=====")
        print(f'Bem-vindo, {usuario["nome"]}!')  
        print("1. Dicas")
        print("2. Metas")
        print("3. Recomendações")
        print("4. Usuários")
        print("5. Sair")

        feature_escolhida = input("Digite um número correspondente à opção: ")

        if feature_escolhida == '1':
            tela_dicas()
        elif feature_escolhida == '2':
            tela_metas(conexao, usuario_id)
        elif feature_escolhida == '3':
            tela_recomendacoes()
        elif feature_escolhida == '4':
            tela_usuarios()
        elif feature_escolhida == '5':
            print("Saindo do programa...")
            conexao.close()
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")



