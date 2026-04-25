"""Dicas sustentáveis e Conteúdo informativo"""
def tela_dicas():
    while True:
        print("\n=====Dicas Sustentáveis=====")
        print('1: vida útil')
        print('2: Manutenção e cuidados')
        print('3: Reutilização e reaproveitamento')
        print('4: Descarte e consumo ')
        print("5. Voltar ao Menu Principal")
        escolha = input("Digite um número correspondente à opção: ")

        if escolha == '1':
            vida_util_tela()
        elif escolha == '2':
            print("Dicas sobre manutenção e cuidados para prolongar a vida útil dos produtos.")
        elif escolha == '3':
            print("Dicas sobre reutilização e reaproveitamento de produtos.")
        elif escolha == '4':
            print("Dicas sobre descarte correto e consumo consciente.")
        elif escolha == '5':
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
Tela de dicas sustentáveis, com opções para vida útil, manutenção e cuidados, reutilização e reaproveitamento,
 descarte e consumo consciente.
"""
def vida_util_tela():
    print("=========Dicas sobre vida útil de aparelhos eletrônicos=========")
    print("""Vida útil de aparelhos eletrônicos

📱 Smartphones

Evite deixar a bateria chegar a 0% ou ficar sempre em 100%.
Use capinha e película para evitar danos físicos.
Reduza brilho da tela para economizar bateria.

📺 TVs

Desligue da tomada quando não estiver em uso por longos períodos.
Evite exposição direta ao sol.
Limpe a tela com pano adequado (sem produtos agressivos).

💻 Computadores/Notebooks

Evite superaquecimento (use em superfícies planas).
Faça limpezas periódicas (poeira interna).
Atualize o sistema para manter o desempenho.

🔊 Caixas de som

Não use no volume máximo por muito tempo.
Proteja contra umidade.
Guarde em local seguro quando não estiver em uso.

🎧 Fones de ouvido

Evite enrolar o fio com força.
Limpe regularmente (especialmente intra-auriculares).
Guarde em estojos para evitar danos.""")
    
"""
Função para exibir dicas sobre a vida útil de aparelhos eletrônicos, incluindo smartphones, TVs, computadores/notebooks,
 caixas de som e fones de ouvido.
"""

asa