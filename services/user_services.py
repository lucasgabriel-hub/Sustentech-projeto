"""Lida com usuários + banco de dados."""

from pages.auth import menu_login_cadastro
from utils.utilidades import limpar_tela

def atualizar_dados_pessoais(conexao, usuario_id):
    print("="*40)
    print('Atualize seus dados pessoais:')
    print("="*40)
    novo_nome = input('Digite seu novo nome: ')
    novo_email = input('Digite seu novo email: ')
    nova_senha = input('Digite sua nova senha: ')

    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, email = ?, senha = ?
        WHERE id = ?
    ''', (novo_nome, novo_email, nova_senha, usuario_id))

    conexao.commit()
    print('Dados pessoais atualizados com sucesso!')
    input('Pressione Enter para retornar ao menu de autenticação:')
    limpar_tela()
    return menu_login_cadastro

def listar_usuarios(conexao):
    print("="*40)
    print('Usuários Cadastrados:')
    print("="*40)

    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, email FROM usuarios')
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f'ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}')
    input('Pressione Enter para retornar ao menu:')
    return limpar_tela()

def deletar_conta(conexao, usuario_id):
    print("="*40)
    print('Deletar Conta')
    print("="*40)
    confirmacao_para_deletar = input('Tem certeza que deseja deletar sua conta?\n ✅sim  ❌não ')
    
    if confirmacao_para_deletar == 'sim':
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
        conexao.commit()
        print('✅ Conta deletada com sucesso!')
        return True  
    else:
        print('❌ Operação cancelada. Sua conta não foi deletada.')
        input('Pressione Enter para retornar ao menu de autenticação:')
        limpar_tela()
        return menu_login_cadastro


    