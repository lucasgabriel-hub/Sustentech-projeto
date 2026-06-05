"""
Tela de recomendações sustentáveis personalizadas.
"""

from utils.utilidades import UI

"""
Questionário para avaliar os hábitos de consumo do usuário e oferecer dicas personalizadas.
Cada pergunta tem opções de resposta que atribuem pontos para calcular um score final.
"""

_PERGUNTAS = [
    {
        "enunciado": "Você costuma desligar aparelhos da tomada quando não está usando?",
        "opcoes": ["1 - Sempre", "2 - Às vezes", "3 - Nunca"],
    },
    {
        "enunciado": "Com que frequência você troca de celular?",
        "opcoes": ["1 - Só quando quebra", "2 - A cada alguns anos", "3 - Todo ano"],
    },
    {
        "enunciado": "Você reutiliza ou recicla eletrônicos antigos?",
        "opcoes": ["1 - Sim", "2 - Às vezes", "3 - Não"],
    },
]

_PONTOS_POR_OPCAO = {"1": 2, "2": 1, "3": 0}

"""
Tela de recomendações sustentáveis personalizadas.
Permite que o usuário responda a um questionário sobre seus hábitos de consumo e oferece dicas personalizadas com base no resultado.
"""

def tela_recomendacoes() -> None:
    while True:
        UI.cabecalho("🌱 Recomendações Sustentáveis Personalizadas 🌱")
        score = 0
        cancelado = False

        for i, pergunta in enumerate(_PERGUNTAS, start=1):
            print(f"\n{i}. {pergunta['enunciado']}")
            for opcao in pergunta["opcoes"]:
                print(f"   {opcao}")

            resposta = input("Resposta: ").strip()
            score += _PONTOS_POR_OPCAO.get(resposta, 0)

            if UI.confirmar("Deseja sair das recomendações?"):
                cancelado = True
                UI.limpar()
                break
            UI.limpar()

        if cancelado:
            break

        _exibir_resultado(score)
        UI.pausar("Pressione Enter para voltar ao menu:")
        UI.limpar()
        break  # encerra após um ciclo completo

"""
Exibe o resultado do questionário e oferece recomendações personalizadas com base na pontuação total.
"""

def _exibir_resultado(score: int) -> None:
    UI.cabecalho("📊 Seu Resultado")

    if score >= 5:
        print("🏆 Parabéns! Você já tem ótimos hábitos sustentáveis!")
        print("💡 Continue assim e inspire outras pessoas!")
    elif score >= 3:
        print("🌱 Você está no caminho certo!")
        print("💡 Dica: pequenas melhorias no dia a dia fazem grande diferença.")
    else:
        print("🚨 Você pode melhorar bastante!")
        print("💡 Recomendações:")
        print("   • Desligue aparelhos da tomada")
        print("   • Evite trocar de celular com frequência")
        print("   • Procure reciclar eletrônicos")
