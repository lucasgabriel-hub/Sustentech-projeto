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
        usuario_id = cursor.lastrowid
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
        return usuario_id
    except sqlite3.IntegrityError:
        print("Erro: O email já está em uso.")
        return None
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
Função para criar a tabela de metas no banco de dados, caso ela ainda não exista.
"""

def criar_tabela_metas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    conexao.commit()
    cursor.close()

"""
Função para armazenar as metas cumpridas ou em andamento no banco de dados, dividindo-as entre diárias, semanais e mensais.
"""
# connections.py

def inserir_metas_padrao(conexao, usuario_id):
    cursor = conexao.cursor()

    metas_padrao = [
        ("diaria", "Desligar luzes ao sair dos ambientes"),
        ("diaria", "Reduzir tempo de banho"),
        ("diaria", "Evitar standby"),

        ("semanal", "Separar lixo reciclável"),
        ("semanal", "Evitar plástico descartável"),
        ("semanal", "Usar transporte alternativo"),

        ("mensal", "Reduzir consumo de energia"),
        ("mensal", "Doar ou reutilizar objetos"),
        ("mensal", "Aprender prática sustentável")
    ]

    for tipo, desc in metas_padrao:
        cursor.execute("""
        INSERT INTO metas (usuario_id, tipo, descricao, status)
        VALUES (?, ?, ?, ?)
        """, (usuario_id, tipo, desc, "pendente"))

    conexao.commit()
