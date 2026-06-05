"""Modelo de domínio: representa um Usuário na aplicação."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Usuario:
    """
    Representa um usuário autenticado na aplicação.
    Centraliza todos os dados e comportamentos do usuário,
    eliminando a necessidade de passar dicionários soltos pelo sistema.
    """

    id: int
    nome: str
    email: str
    # Senha nunca é armazenada em texto puro na memória após o login
    _senha_hash: str = field(default="", repr=False)

    
    # Validações de negócio relacionadas ao usuário

    @staticmethod
    def validar_nome(nome: str) -> bool:
        """Nome deve ter entre 3 e 20 caracteres."""
        return 3 <= len(nome.strip()) <= 20

    @staticmethod
    def validar_email(email: str) -> bool:
        """Apenas emails @gmail.com são aceitos no momento."""
        return email.strip().endswith("@gmail.com")

    @staticmethod
    def validar_senha(senha: str) -> bool:
        """Senha deve ter pelo menos 6 caracteres."""
        return len(senha) >= 6

    # Helpers de exibição
    
    def saudacao(self) -> str:
        return f"Bem-vindo(a), {self.nome}! 🌱"

    def __str__(self) -> str:
        return f"Usuario(id={self.id}, nome={self.nome!r}, email={self.email!r})"