"""Controla menus e navegação. login, cadastro, sair"""

from pages.Dicas import tela_dicas
from pages.metas import tela_metas
from pages.recomendacoes import tela_recomendacoes
from pages.usuarios import tela_usuarios
from database.connection import conectar_banco
from pages.quiz import tela_quiz
from utils.utilidades import limpar_tela
from pages.loja import tela_loja
from pages.rotas import rotas_descarte

def menu_principal(conexao, usuario):
    usuario_id = usuario["id"]
    conexao = conectar_banco()
    
    while True:
        print("="*40)
        print('Menu Principal')
        print("="*40)
        print(f'Bem-vindo, {usuario["nome"]}!')  
        print('1. Dicas')
        print('2. Metas')
        print('3. Quiz')
        print('4. Recomendações')
        print('5. Usuários')
        print('6. Loja')
        print('7. Rotas de Descarte')
        print('8. Sair')
        print("-"*40)

        feature_escolhida = input('Digite um número correspondente à opção: ')

        if feature_escolhida == '1':
            limpar_tela()
            tela_dicas()
        elif feature_escolhida == '2':
            limpar_tela()
            tela_metas(conexao, usuario_id)
        elif feature_escolhida == '3':
            limpar_tela()
            tela_quiz()
        elif feature_escolhida == '4':
            limpar_tela()
            tela_recomendacoes()
        elif feature_escolhida == '5':
            limpar_tela()
            tela_usuarios(conexao, usuario_id)
        elif feature_escolhida == '6':
            limpar_tela()
            tela_loja()
        elif feature_escolhida == '7':
            limpar_tela()
            rotas_descarte()
        elif feature_escolhida == '8':
            print('Saindo do programa...')
            conexao.close()
            break
        else:
            print('Opção inválida. Por favor, escolha uma das opções acima.')
            limpar_tela()



