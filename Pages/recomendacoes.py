"""Recomendar ações e Sugerir melhorias"""

from utils.utilidades import limpar_tela

def tela_recomendacoes():

    print("="*40)
    print('🌱 Recomendações Sustentáveis Personalizadas 🌱')
    print("="*40)

    score = 0

    # Pergunta 1
    print('1. Você costuma desligar aparelhos da tomada quando não está usando?')
    print('1 - Sempre')
    print('2 - Às vezes')
    print('3 - Nunca')
    r1 = input('Resposta: ')

    if r1 == "1":
        score += 2
    elif r1 == "2":
        score += 1

    # Pergunta 2
    print('2. Com que frequência você troca de celular?')
    print('1 - Só quando quebra')
    print('2 - A cada alguns anos')
    print('3 - Todo ano')
    r2 = input('Resposta: ')

    if r2 == "1":
        score += 2
    elif r2 == "2":
        score += 1

    # Pergunta 3
    print('\n3. Você reutiliza ou recicla eletrônicos antigos?')
    print('1 - Sim')
    print('2 - Às vezes')
    print('3 - Não')
    r3 = input('Resposta: ')

    if r3 == "1":
        score += 2
    elif r3 == "2":
        score += 1

    # Resultado
    limpar_tela()
    print('📊 Seu resultado:')
    
    if score >= 5:
        print('Parabéns! Você já tem hábitos sustentáveis!')
        print('💡 Continue assim e tente influenciar outras pessoas!')
    
    elif score >= 3:
        print('Você está no caminho certo !!!')
        print('💡 Dica: tente melhorar pequenos hábitos no dia a dia.')
    
    else:
        print('Você pode melhorar bastante 🚨')
        print('💡 Recomendações:')
        print('- Desligue aparelhos da tomada')
        print('- Evite trocar de celular com frequência')
        print('- Procure reciclar eletrônicos')

    input('Pressione Enter para voltar ao menu:')