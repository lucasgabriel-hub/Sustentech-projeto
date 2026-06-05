"""Tela do quiz de sustentabilidade."""

from services.quiz_service import QuizService, PONTOS_POR_ACERTO
from utils.utilidades import UI


def tela_quiz() -> None:
    """
    Exibe o quiz de sustentabilidade, permitindo que o usuário responda perguntas e acompanhe sua pontuação.
    """
    service = QuizService()
    perguntas = service.get_perguntas()
    pontuacao = 0

    UI.cabecalho("Quiz de Sustentabilidade 🌱")

    for numero, pergunta in enumerate(perguntas, start=1):
        pergunta.exibir(numero)

        resposta = input(
            'Sua resposta (ou "MENU" para sair): '
        ).strip().upper()

        if resposta == "MENU":
            UI.limpar()
            return

        if pergunta.verificar_resposta(resposta):
            UI.sucesso("Resposta correta!")
            pontuacao += PONTOS_POR_ACERTO
        else:
            UI.erro(f"Incorreta! A resposta certa era: {pergunta.resposta_correta}")

        UI.pausar("Pressione Enter para a próxima pergunta...")
        UI.limpar()

    print(f"\n🎉 Pontuação final: {pontuacao} pontos")
    print(service.calcular_nivel(pontuacao))
    UI.pausar("Pressione Enter para voltar ao menu:")
    UI.limpar()
