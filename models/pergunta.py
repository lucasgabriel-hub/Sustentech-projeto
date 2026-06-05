"""
Modelo de domínio: representa uma Pergunta do quiz.
"""

from dataclasses import dataclass

@dataclass
class Pergunta:
    """
    Encapsula uma pergunta do quiz com suas opções e resposta correta.
    Antes, o acesso era feito via dict keys.
    Com essa classe, o acesso é tipado e o IDE consegue autocompletar.
    """

    enunciado: str
    opcoes: list[str]
    resposta_correta: str

    def verificar_resposta(self, resposta: str) -> bool:
        return resposta.strip().upper() == self.resposta_correta.upper()

    def exibir(self, numero: int) -> None:
        print(f"\nPergunta {numero}: {self.enunciado}")
        for opcao in self.opcoes:
            print(f"  {opcao}")
