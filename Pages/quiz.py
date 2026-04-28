"""Mostrar perguntas, Receber respostas e Calcular pontuação"""

from services.quiz_service import perguntas

def tela_quiz():
    perguntas
    pontuacao = 0

    print('=' * 40)
    print("Quiz de Sustentável")
    print('=' * 40)

    for numero_da_pergunta, pergunta in enumerate(perguntas, start=1):
        print(f"\nPergunta {numero_da_pergunta}: {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)

        resposta_usuario = input("Digite a letra da resposta correta: ").strip().upper()

        if resposta_usuario == pergunta['resposta']:
            print("✅ Resposta correta!")
            pontuacao += 5
        else:
            print(f"❌ Resposta incorreta! A resposta correta é: {pergunta['resposta']}")

    print(f'PARABÉNS!🎉 Sua pontuação final é: {pontuacao}')
    input("Pressione Enter para voltar ao menu principal:")