"""Atualizar dados, Listar usuários e Perfil"""

from services.user_services import atualizar_dados_pessoais
from services.user_services import listar_usuarios
from services.user_services import deletar_conta
from utils.utilidades import limpar_tela

def tela_usuarios(conexao, usuario_id):
    print("="*40)
    print('👥 Gerenciamento de Usuários 👥')
    print("="*40)

    print('1. Atualizar Dados Pessoais')
    print('2. Listar Usuários Cadastrados')
    print('3. deletar minha conta')
    print('4. Voltar ao Menu Principal')
    print("-"*40)

    escolha_do_usuario = input('Escolha uma opção: ')
    if escolha_do_usuario == '1':
        atualizar_dados_pessoais(conexao)
        
    elif escolha_do_usuario == '2':
        listar_usuarios(conexao)
        
    elif escolha_do_usuario == '3':
        deletar_conta(conexao, usuario_id)
        
    elif escolha_do_usuario == '4':
        input('pressione enter para voltar ao menu: ')
        



    
