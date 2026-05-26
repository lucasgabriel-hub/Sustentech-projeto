"""Mostrar perguntas, Receber respostas e Calcular pontuação"""

from services.quiz_service import perguntas
from utils.utilidades import limpar_tela

def tela_quiz():
    perguntas
    pontuacao = 0

    print('=' * 40)
    print('Quiz de Sustentável')
    print('=' * 40)

    for numero_da_pergunta, pergunta in enumerate(perguntas, start=1):
        print(f"\nPergunta {numero_da_pergunta}: {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)

        resposta_usuario = input('Digite a letra da resposta correta ou digite "MENU" para voltar ao menu principal: ').strip().upper()

        if resposta_usuario == 'MENU':
            limpar_tela()
            return
        elif resposta_usuario == pergunta['resposta']:
            print('✅ Resposta correta!')
            pontuacao += 5
        else:
            print(f'❌ Resposta incorreta! A resposta correta é: {pergunta["resposta"]}')
        
        input('Pressione Enter para continuar para a próxima pergunta...')
        limpar_tela()

    print(f'PARABÉNS!🎉 Sua pontuação final é: {pontuacao}')
    input('Pressione Enter para voltar ao menu principal:')
    limpar_tela()