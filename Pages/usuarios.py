"""Atualizar dados, Listar usuários e Perfil"""

from services.user_services import atualizar_dados_pessoais
from services.user_services import listar_usuarios
from services.user_services import deletar_conta

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
        print('Opção de atualizar dados pessoais selecionada.')
        # Aqui você pode adicionar a lógica para atualizar os dados pessoais do usuário
    elif escolha_do_usuario == '2':
        print('Opção de listar usuários cadastrados selecionada.')
        # Aqui você pode adicionar a lógica para listar os usuários cadastrados
    elif escolha_do_usuario == '3':
        print('Opção de deletar conta selecionada.')
        # Aqui você pode adicionar a lógica para deletar a conta do usuário
    elif escolha_do_usuario == '4':
        print('Voltando ao menu principal...')
        # Aqui você pode adicionar a lógica para voltar ao menu principal
        



    
