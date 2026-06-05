"""Repositório de Usuários — toda comunicação com a tabela `usuarios`."""

import sqlite3
from typing import Optional
from models.usuario import Usuario, UsuarioCadastro
from models.meta import Meta

class UsuarioRepository:
    """
    Isola todas as queries SQL relacionadas a usuários.
    """

    def __init__(self, conexao: sqlite3.Connection) -> None:
        self._conn = conexao

    """
    Cria a tabela `usuarios` se ela ainda não existir.
    """
    
    def criar_tabela(self) -> None:
        self._conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    UNIQUE NOT NULL,
                senha TEXT    NOT NULL
            )
        ''')
        self._conn.commit()

    """
    funções de escrita: cadastrar, atualizar, deletar
    """

    def cadastrar(self, dto: UsuarioCadastro) -> Optional[int]:
        """
        Persiste um novo usuário.
        Retorna o id gerado, ou None se o email já estiver em uso.
        """
        try:
            cursor = self._conn.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (dto.nome, dto.email, dto.senha),
            )
            self._conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None

    def atualizar(self, usuario_id: int, nome: str, email: str, senha: str) -> None:
        self._conn.execute(
            "UPDATE usuarios SET nome=?, email=?, senha=? WHERE id=?",
            (nome, email, senha, usuario_id),
        )
        self._conn.commit()

    def deletar(self, usuario_id: int) -> None:
        self._conn.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
        self._conn.commit()

    """
    funções de leitura: buscar por id, email+senha, listar todos
    """

    def buscar_por_credenciais(self, email: str, senha: str) -> Optional[Usuario]:
        """Retorna um objeto Usuario ou None — nunca uma tupla crua."""
        row = self._conn.execute(
            "SELECT id, nome, email, senha FROM usuarios WHERE email=? AND senha=?",
            (email, senha),
        ).fetchone()

        if row is None:
            return None
        return Usuario(id=row[0], nome=row[1], email=row[2], _senha_hash=row[3])

    def listar_todos(self) -> list[Usuario]:
        rows = self._conn.execute(
            "SELECT id, nome, email FROM usuarios"
        ).fetchall()
        return [Usuario(id=r[0], nome=r[1], email=r[2]) for r in rows]
