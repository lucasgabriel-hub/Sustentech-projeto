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

@dataclass
class UsuarioCadastro:
    """
    DTO (Data Transfer Object) usado apenas durante o fluxo de cadastro,
    antes de o registro ser persistido no banco.
    """

    nome: str
    email: str
    senha: str

    def is_valido(self) -> tuple[bool, list[str]]:
        """
        Retorna (valido, lista_de_erros).
        Facilita exibir todas as mensagens de erro de uma vez.
        """
        erros: list[str] = []

        if not Usuario.validar_nome(self.nome):
            erros.append("Nome deve ter entre 3 e 20 caracteres.")
        if not Usuario.validar_email(self.email):
            erros.append("Email deve terminar com @gmail.com.")
        if not Usuario.validar_senha(self.senha):
            erros.append("Senha deve ter pelo menos 6 caracteres.")

        return (len(erros) == 0, erros)
