"""
Funções e constantes auxiliares reutilizáveis.
"""

import os

"""
Dicionário de emojis para uso em mensagens de terminal.
"""

EMOJIS = {
    "ok":       "✅",
    "erro":     "❌",
    "alerta":   "⚠️",
    "recicla":  "♻️",
    "planta":   "🌱",
    "stats":    "📊",
    "dica":     "💡",
    "urgente":  "🚨",
    "festa":    "🎉",
    "usuarios": "👥",
    "alvo":     "🎯",
}

LINHA  = "=" * 40
DIVISA = "-" * 40


"""
Funções e constantes auxiliares reutilizáveis.
"""

class UI:
    """
    Centraliza operações de terminal para facilitar uma futura
    migração para interface gráfica ou web: só este arquivo muda.
    """

    @staticmethod
    def limpar() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def pausar(mensagem: str = "Pressione Enter para continuar...") -> None:
        input(mensagem)

    @staticmethod
    def cabecalho(titulo: str) -> None:
        print(LINHA)
        print(titulo)
        print(LINHA)

    @staticmethod
    def separador() -> None:
        print(DIVISA)

    @staticmethod
    def erro(mensagem: str) -> None:
        print(f"{EMOJIS['erro']} {mensagem}")

    @staticmethod
    def sucesso(mensagem: str) -> None:
        print(f"{EMOJIS['ok']} {mensagem}")

    @staticmethod
    def aviso(mensagem: str) -> None:
        print(f"{EMOJIS['alerta']} {mensagem}")

    @staticmethod
    def confirmar(pergunta: str) -> bool:
        """Retorna True se o usuário digitar 'sim'."""
        while True:
            resposta = input(f"{pergunta} (sim/não): ").strip().lower()
            if resposta == "sim":
                return True
            elif resposta in ("não", "nao"):
                return False
            print("Resposta inválida. Digite 'sim' ou 'não'.")

def limpar_tela():
    #print("\n"* 50")
    os.system('cls' if os.name == 'nt' else 'clear')

def tamanho(texto):
    if len(texto) < 3 or len(texto) > 20:
        return False
    return True

def confirmarsaidarecomendacao():
    while True:
        resposta = input('Deseja sair da seção de recomendações? ("sim" ou "não"): ')
        if resposta == 'sim':
            return True
        elif resposta == 'não':
            return False
        else:
            print('Resposta invalida. Por favor, responda com "sim" ou "não".')
    