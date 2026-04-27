"""Responsável pela conexão com o SQLite."""
import sqlite3
from configurations.config import DB_PATH

def conectar_banco():
    conexao = sqlite3.connect(DB_PATH)
    return conexao

def criar_tabela_usuarios(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conexao.commit()
    cursor.close()

"""
Função para criar a tabela de usuários no banco de dados, caso ela ainda não exista.
Essa tabela armazenará as informações dos usuários, como nome, email e senha.
"""

def cadastrar_usuario(conexao, nome, email, senha):
    cursor = conexao.cursor()
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O email já está em uso.")
    finally:
        cursor.close()

"""
função para verificar se o email e senha correspondem a um usuário cadastrado no banco de dados.
"""

def verificar_usuario(conexao, email, senha):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios WHERE email = ? AND senha = ?
    ''', (email, senha))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

"""
Função para fechar a conexão com o banco de dados quando não for mais necessária.
"""

def fechar_conexao(conexao):
    if conexao:
        conexao.close()

"""
Função para armazenar as metas cumpridas ou em andamento no banco de dados, dividindo-as entre diárias, semanais e mensais.
"""
def criar_tabela_metas(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            categoria TEXT,
            descricao TEXT,
            status TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    conexao.commit()
    cursor.close()
"""
função para informar se a meta foi cumprida ou está em andamento, e armazenar essa informação no banco de dados.
"""
def registrar_meta(conexao, usuario_id, categoria, descricao, status):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO metas (usuario_id, categoria, descricao, status) VALUES (?, ?, ?, ?)
    ''', (usuario_id, categoria, descricao, status))
    conexao.commit()
    cursor.close()

"""
tabela que armazena as informações sobre metas separando em: diários, semanais e mensais,
"""
def obter_metas_por_usuario(conexao, usuario_id):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT categoria, descricao, status FROM metas WHERE usuario_id = ?
    ''', (usuario_id,))
    metas = cursor.fetchall()
    cursor.close()
    return metas

