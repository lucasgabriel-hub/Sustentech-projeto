"""Criar meta sustentável e Acompanhar progresso"""

def tela_metas():
   while True:
        print("\n=====Sistema de Metas Sustentáveis=====")
        print('1 Diária')
        print('2 Semanal')
        print('3 Mensal')
        print('4 Voltar para o menu principal')
    
        meta_escolhida = input("escolha a aba de metas que deseja entrar: ")

        if meta_escolhida == '1':
            meta_diaria()
        
        elif meta_escolhida == '2':
            meta_semanal()
    
        elif meta_escolhida == '3':
            meta_mensal()

        elif meta_escolhida == '4':
            menu_principal()

        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
função que repete as metas para cada categoria (diária, semanal e mensal)
 e permite que o usuário escolha qual categoria deseja acessar.
"""
            
def meta_diaria():
    print('1: Desligar luzes ao sair dos ambientes')
    print('2: Reduzir tempo de banho (até 10 minutos)')
    print('3: Evitar deixar aparelhos em standby')
        
def meta_semanal():
    print('1: Separar lixo reciclável corretamente')
    print('2: Evitar usar plástico descartável durante a semana')
    print('3: Usar transporte alternativo (andar, bicicleta ou transporte público pelo menos 1x)')
def meta_mensal():
    print('1: Reduzir o consumo de energia (comparar com o mês anterior)')
    print('2: Doar ou reutilizar objetos/eletrônicos que não usa mais')
    print('3: Aprender e aplicar uma nova prática sustentável')

"""
funções para criar metas, acompanhar o progresso e registrar as metas cumpridas ou em andamento.
"""

"""
Criar um registro de metas que já foram cumpridas e as que ainda estão em andamento.
"""
