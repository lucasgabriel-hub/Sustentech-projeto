"""Dicas sustentáveis e Conteúdo informativo"""

def tela_dicas():
    while True:
        print("\n=====Dicas Sustentáveis=====")
        print('1: vida útil')
        print('2: Manutenção e cuidados')
        print('3: Reutilização e reaproveitamento')
        print('4: Descarte e consumo ')
        print("5. Voltar ao Menu Principal")
        dica_escolhida = input("Digite um número correspondente às dicas que deseja ver: ")

        if dica_escolhida == '1':
            vida_util_tela()
        elif dica_escolhida == '2':
            manutencao_cuidados()
        elif dica_escolhida == '3':
            reutilizacao_reaproveitamento()
        elif dica_escolhida == '4':
            descarte_consumo_consciente()
        elif dica_escolhida == '5':
            menu_principal()
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

def manutencao_cuidados():
    print("=========Dicas sobre manutenção e cuidados=========")
    print("""
Faça limpezas regulares para evitar acúmulo de poeira.
Use carregadores originais ou certificados.
Evite quedas e impactos.
Não exponha aparelhos à água ou calor excessivo.
Atualize softwares e antivírus para manter o funcionamento correto.""")

"""
Função para exibir dicas sobre manutenção e cuidados para prolongar a vida útil dos produtos,
 incluindo limpezas regulares,
"""
def reutilizacao_reaproveitamento():
    print("=========Dicas sobre reutilização e reaproveitamento=========")
    print("""Transforme celulares antigos em câmeras de segurança ou despertadores.
Use notebooks antigos para estudos básicos ou servidores simples.
Aproveite peças (cabos, carregadores, HDs).
Doe aparelhos que ainda funcionam.
Reutilize caixas e embalagens para organização.""")
    
"""
Função para exibir dicas sobre reutilização e reaproveitamento de produtos.
"""
def descarte_consumo_consciente():
    print("=========Dicas sobre descarte e consumo consciente=========")
    print("""Nunca jogue eletrônicos no lixo comum (contêm materiais tóxicos).
Procure pontos de coleta de lixo eletrônico na sua cidade.
Prefira marcas com compromisso ambiental.
Evite comprar por impulso — só adquira o necessário.
Dê preferência a produtos duráveis e com garantia maior.""")
"""
Função para exibir dicas sobre descarte e consumo consciente de produtos eletrônicos.
"""
