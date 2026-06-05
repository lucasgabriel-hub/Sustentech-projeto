"""Lógica e banco de perguntas do quiz."""

from models.pergunta import Pergunta

# Pontos concedidos por acerto
PONTOS_POR_ACERTO = 5


class QuizService:
    """
    Centraliza as perguntas e a lógica de pontuação.
    Para adicionar novas perguntas, edite apenas _BANCO_PERGUNTAS.
    """

    _BANCO_PERGUNTAS: list[Pergunta] = [
        Pergunta(
            enunciado="Qual atitude ajuda a aumentar a vida útil de um smartphone?",
            opcoes=["A) Usar enquanto carrega sempre",
                    "B) Deixar descarregar até 0% frequentemente",
                    "C) Evitar superaquecimento",
                    "D) Trocar todo ano"],
            resposta_correta="C",
        ),
        Pergunta(
            enunciado="O que significa reciclar?",
            opcoes=["A) Jogar no lixo comum",
                    "B) Reutilizar um material para criar outro produto",
                    "C) Queimar resíduos",
                    "D) Enterrar resíduos"],
            resposta_correta="B",
        ),
        Pergunta(
            enunciado="Qual desses materiais é reciclável?",
            opcoes=["A) Papel",
                    "B) Restos de comida",
                    "C) Papel higiênico usado",
                    "D) Fraldas descartáveis"],
            resposta_correta="A",
        ),
        Pergunta(
            enunciado="Qual prática economiza energia elétrica?",
            opcoes=["A) Deixar luz acesa o dia todo",
                    "B) Tirar aparelhos da tomada quando não usados",
                    "C) Usar todos os aparelhos ao mesmo tempo",
                    "D) Abrir a geladeira várias vezes"],
            resposta_correta="B",
        ),
        Pergunta(
            enunciado="O que fazer com eletrônicos antigos?",
            opcoes=["A) Jogar no lixo comum",
                    "B) Queimar",
                    "C) Levar para pontos de coleta",
                    "D) Enterrar no quintal"],
            resposta_correta="C",
        ),
        Pergunta(
            enunciado="Qual dessas atitudes ajuda o meio ambiente?",
            opcoes=["A) Usar sacolas plásticas sempre",
                    "B) Comprar sem necessidade",
                    "C) Reutilizar materiais",
                    "D) Desperdiçar água"],
            resposta_correta="C",
        ),
        Pergunta(
            enunciado="O que é consumo consciente?",
            opcoes=["A) Comprar tudo que quiser",
                    "B) Comprar pensando no impacto ambiental",
                    "C) Comprar só produtos caros",
                    "D) Não comprar nada"],
            resposta_correta="B",
        ),
        Pergunta(
            enunciado="Qual desses reduz o desperdício de água?",
            opcoes=["A) Banhos longos",
                    "B) Escovar os dentes com torneira aberta",
                    "C) Fechar a torneira ao escovar os dentes",
                    "D) Lavar calçada com mangueira"],
            resposta_correta="C",
        ),
        Pergunta(
            enunciado="Qual dessas práticas ajuda na sustentabilidade dos eletrônicos?",
            opcoes=["A) Trocar de celular todo ano",
                    "B) Fazer manutenção regular",
                    "C) Jogar fora ao primeiro problema",
                    "D) Não usar capa protetora"],
            resposta_correta="B",
        ),
        Pergunta(
            enunciado="O que significa reutilizar?",
            opcoes=["A) Jogar fora",
                    "B) Usar novamente um item sem transformá-lo",
                    "C) Queimar",
                    "D) Reciclar automaticamente"],
            resposta_correta="B",
        ),
    ]

    def get_perguntas(self) -> list[Pergunta]:
        """
        Retorna a lista de perguntas do quiz.
        Para adicionar novas perguntas, edite apenas _BANCO_PERGUNTAS.
        """
        return self._BANCO_PERGUNTAS

    def calcular_nivel(self, pontuacao: int) -> str:
        total_possivel = len(self._BANCO_PERGUNTAS) * PONTOS_POR_ACERTO
        percentual = pontuacao / total_possivel if total_possivel > 0 else 0

        """
        Calcula o nível do usuário com base na pontuação.
        """
        if percentual >= 0.8:
            return "🏆 Especialista em Sustentabilidade!"
        elif percentual >= 0.5:
            return "🌱 Em desenvolvimento — continue assim!"
        else:
            return "🚨 Iniciante — explore as dicas e tente novamente!"