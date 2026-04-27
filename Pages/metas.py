"""Criar meta sustentável e Acompanhar progresso"""

"""
Tela de metas sustentáveis, com opções para metas diárias, semanais e mensais, 
além de permitir concluir metas e acompanhar o progresso.
"""

def tela_metas():
   while True:
        print("="*40)
        print("Metas Sustentáveis")
        print("="*40)
        print('1 Diária')
        print('2 Semanal')
        print('3 Mensal')
        print('4 Voltar para o menu principal')
    
        meta_escolhida = input("escolha a aba de metas que deseja entrar: ")

        if meta_escolhida == '1':
            menu_tipo("diária")
        
        elif meta_escolhida == '2':
            menu_tipo("semanal")
    
        elif meta_escolhida == '3':
            menu_tipo("mensal")

        elif meta_escolhida == '4':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
função para concluir uma meta, alterando seu status para "concluída".
"""

def menu_tipo(tipo):
    while True:
        print("-"*35)
        print(f" METAS {tipo.upper()}")
        print("-"*35)
        print("1 Ver metas")
        print("2 Concluir uma meta")
        print("0 Voltar")
        print("-"*35)

        opcao = input("Escolha se deseja ver as metas ou concluir uma meta: ")

        if opcao == "1":
            mostrar_metas(tipo)
        elif opcao == "2":
            concluir_meta(tipo)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")

"""
função para mostrar as metas de um tipo específico, exibindo a descrição e o status de cada meta.
"""

def mostrar_metas(tipo):
    lista = metas[tipo]

    print("\n" + "="*40)
    print(f"📊 METAS {tipo.upper()}")
    print("="*40)

    for i, meta in enumerate(lista, start=1):
        status = "✅" if meta["status"] == "concluída" else "⏳"
        print(f"{i}. {meta['descricao']}")
        print(f"   Status: {status} {meta['status']}")
        print("-"*40)

    return lista

"""
função para concluir uma meta, alterando seu status para "concluída".
"""

def concluir_meta(tipo):
    lista = mostrar_metas(tipo)

    try:
        opcao = int(input(" Digite o número da meta concluída: ")) - 1

        if lista[opcao]["status"] == "concluída":
            print("⚠️ Essa meta já foi concluída!")
        else:
            lista[opcao]["status"] = "concluída"
            print("🎉 Parabéns! Meta concluída!")

    except (IndexError, ValueError):
        print("❌ Opção inválida!")

"""
lista de metas sustentáveis, divididas em categorias diária, semanal e mensal.
Cada meta tem uma descrição e um status (pendente ou concluída).
"""
            
metas = {
    "diaria": [
        {"descricao": "Desligar luzes ao sair dos ambientes", "status": "pendente"},
        {"descricao": "Reduzir tempo de banho (até 10 minutos)", "status": "pendente"},
        {"descricao": "Evitar deixar aparelhos em standby", "status": "pendente"}
    ],
    
    "semanal": [
        {"descricao": "Separar lixo reciclável corretamente", "status": "pendente"},
        {"descricao": "Evitar usar plástico descartável durante a semana", "status": "pendente"},
        {"descricao": "Usar transporte alternativo pelo menos 1x", "status": "pendente"}
    ],
    
    "mensal": [
        {"descricao": "Reduzir o consumo de energia", "status": "pendente"},
        {"descricao": "Doar ou reutilizar objetos/eletrônicos", "status": "pendente"},
        {"descricao": "Aprender uma nova prática sustentável", "status": "pendente"}
    ]
}
