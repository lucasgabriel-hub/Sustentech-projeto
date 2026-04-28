"""Criar meta sustentável e Acompanhar progresso"""

"""
Tela de metas sustentáveis, com opções para metas diárias, semanais e mensais, 
além de permitir concluir metas e acompanhar o progresso.
"""

def tela_metas(conexao, usuario_id):
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
            menu_tipo(conexao, usuario_id, "diaria")
        
        elif meta_escolhida == '2':
            menu_tipo(conexao, usuario_id, "semanal")
    
        elif meta_escolhida == '3':
            menu_tipo(conexao, usuario_id, "mensal")

        elif meta_escolhida == '4':
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

"""
função para concluir uma meta, alterando seu status para "concluída".
"""

def menu_tipo(conexao, usuario_id, tipo):
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
            mostrar_metas(conexao, usuario_id, tipo)
        elif opcao == "2":
            concluir_meta(conexao, usuario_id, tipo)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida, escolha novamente!")

"""
função para mostrar as metas de um tipo específico, exibindo a descrição e o status de cada meta.
"""

def mostrar_metas(conexao, usuario_id, tipo):
    cursor = conexao.cursor()
    cursor.execute("SELECT id, descricao, status FROM metas WHERE usuario_id = ? AND tipo = ?", 
                   (usuario_id, tipo))
    metas = cursor.fetchall()
    cursor.close()

    print("\n" + "="*40)
    print(f"📊 METAS {tipo.upper()}")
    print("="*40)

    for i, meta in enumerate(metas, start=1):
        status = "✅" if meta[2] == "concluída" else "⏳"
        print(f"{i}. {meta[1]}")
        print(f"   Status: {status} {meta[2]}")
        print("-"*40)
    input("Pressione Enter para voltar...")

    return metas

"""
função para concluir uma meta, alterando seu status para "concluída".
"""

def concluir_meta(conexao, usuario_id, tipo):
    meta = mostrar_metas(conexao, usuario_id, tipo)

    try:
        opcao = int(input("Digite o número da meta que deseja concluir: "))
        if opcao < 0 or opcao >= len(meta):
            print("❌ Opção inválida!")
            return
        
        id_meta = meta[opcao - 1][0]

        cursor = conexao.cursor()
        cursor.execute("UPDATE metas SET status = 'concluída' WHERE id = ? AND usuario_id = ?", 
                       (id_meta, usuario_id))
        
        conexao.commit()
            
        print("🎉 Parabéns! Meta concluída!")

    except (IndexError, ValueError):
        print("❌ Opção inválida!")


