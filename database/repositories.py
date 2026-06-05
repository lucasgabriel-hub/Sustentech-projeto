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

class MetaRepository:
    """
    Isola todas as queries SQL relacionadas a metas.
    """

    def __init__(self, conexao: sqlite3.Connection) -> None:
        self._conn = conexao

    def criar_tabela(self) -> None:
        self._conn.execute('''
            CREATE TABLE IF NOT EXISTS metas (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                tipo       TEXT    NOT NULL,
                descricao  TEXT    NOT NULL,
                status     TEXT    NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            )
        ''')
        self._conn.commit()

    """
    funções de escrita: inserir metas padrão
    """

    def inserir_metas_padrao(self, usuario_id: int) -> None:
        """
        Insere as metas iniciais de um novo usuário.
        """
        metas = Meta.metas_padrao(usuario_id)
        self._conn.executemany(
            "INSERT INTO metas (usuario_id, tipo, descricao, status) VALUES (?,?,?,?)",
            [(m.usuario_id, m.tipo.value, m.descricao, m.status.value) for m in metas],
        )
        self._conn.commit()

    def listar_por_tipo(self, usuario_id: int, tipo: str) -> list[Meta]:
        """
        Retorna as metas do usuário filtradas por tipo (ex: 'reciclagem').
        """
        from models.meta import TipoMeta, StatusMeta
        rows = self._conn.execute(
            "SELECT id, descricao, status FROM metas WHERE usuario_id=? AND tipo=?",
            (usuario_id, tipo),
        ).fetchall()
        return [
            Meta(
                id=r[0],
                usuario_id=usuario_id,
                tipo=TipoMeta(tipo),
                descricao=r[1],
                status=StatusMeta(r[2]),
            )
            for r in rows
        ]

    def concluir(self, meta_id: int, usuario_id: int) -> None:
        """
        Marca a meta como concluída.
        """
        self._conn.execute(
            "UPDATE metas SET status='concluída' WHERE id=? AND usuario_id=?",
            (meta_id, usuario_id),
        )
        self._conn.commit()

class TokenRepository:
    """
    Isola todas as queries SQL relacionadas à tabela `tokens`.
    """

    def __init__(self, conexao) -> None:
        self._conn = conexao

    def criar_tabela(self) -> None:
        self._conn.execute('''
            CREATE TABLE IF NOT EXISTS tokens (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id  INTEGER NOT NULL,
                meta_id     INTEGER NOT NULL,
                quantidade  INTEGER NOT NULL,
                descricao   TEXT    NOT NULL,
                criado_em   TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                FOREIGN KEY (meta_id)    REFERENCES metas    (id)
            )
        ''')
        self._conn.commit()

    """
    funções de escrita: registrar recompensas de tokens
    """

    def registrar(self, usuario_id: int, meta_id: int,
                  quantidade: int, descricao: str) -> None:
        """Persiste uma recompensa de tokens para o usuário."""
        self._conn.execute(
            """INSERT INTO tokens (usuario_id, meta_id, quantidade, descricao)
               VALUES (?, ?, ?, ?)""",
            (usuario_id, meta_id, quantidade, descricao),
        )
        self._conn.commit()

    """
    funções de leitura: consultar saldo e histórico de transações
    """

    def saldo(self, usuario_id: int) -> int:
        """
        Retorna o total acumulado de tokens do usuário.
        """
        row = self._conn.execute(
            "SELECT COALESCE(SUM(quantidade), 0) FROM tokens WHERE usuario_id=?",
            (usuario_id,),
        ).fetchone()
        return int(row[0])

    def historico(self, usuario_id: int, limite: int = 10):
        """
        Retorna os últimos `limite` registros de tokens, do mais recente.
        """
        from models.token import Token
        rows = self._conn.execute(
            """SELECT id, usuario_id, meta_id, quantidade, descricao, criado_em
               FROM tokens
               WHERE usuario_id=?
               ORDER BY criado_em DESC
               LIMIT ?""",
            (usuario_id, limite),
        ).fetchall()
        return [
            Token(id=r[0], usuario_id=r[1], meta_id=r[2],
                  quantidade=r[3], descricao=r[4], criado_em=r[5])
            for r in rows
        ]