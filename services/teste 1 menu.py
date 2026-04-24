# core/menu.py

from core.session import usuario_logado

from pages.usuarios import tela_usuarios
from pages.dicas import tela_dicas
from pages.quiz import tela_quiz
from pages.metas import tela_metas
from pages.recomendacoes import tela_recomendacoes


def exibir_menu():
    print("\n" + "=" * 30)
    print("        SUSTENTECH")
    print("=" * 30)

    try:
        if usuario_logado and "nome" in usuario_logado:
            print(f"Usuário: {usuario_logado['nome']}")
        else:
            print("Usuário: Visitante")
    except Exception:
        print("Usuário: (erro ao carregar sessão)")

    print("\nEscolha uma opção:")
    print("1. Usuários")
    print("2. Dicas Sustentáveis")
    print("3. Quiz")
    print("4. Metas (login necessário)")
    print("5. Recomendações (login necessário)")
    print("0. Sair")


def obter_opcao():
    try:
        opcao = input("\nDigite sua opção: ").strip()
        return opcao
    except EOFError:
        print("\n⚠️ Entrada inesperada encerrada.")
        return "0"
    except KeyboardInterrupt:
        print("\n⚠️ Operação interrompida pelo usuário.")
        return None


def validar_opcao(opcao, opcoes_validas):
    if opcao is None:
        return False

    if opcao not in opcoes_validas:
        print("\n❌ Opção inválida. Digite um número válido.")
        return False

    return True


def verificar_permissao(opcao):
    # Protege áreas que exigem login
    if opcao in ["4", "5"]:
        if not usuario_logado:
            print("\n🔒 Acesso negado. Faça login primeiro.")
            return False
    return True


def executar_opcao(opcao, opcoes):
    try:
        funcao = opcoes.get(opcao)

        if funcao:
            funcao()
        else:
            print("\n❌ Função não encontrada.")
    except Exception as e:
        print("\n🚨 Ocorreu um erro ao executar a opção.")
        print(f"Detalhes técnicos: {e}")


def navegar():
    opcoes = {
        "1": tela_usuarios,
        "2": tela_dicas,
        "3": tela_quiz,
        "4": tela_metas,
        "5": tela_recomendacoes,
        "0": None
    }

    while True:
        exibir_menu()

        opcao = obter_opcao()

        if opcao == "0":
            print("\nEncerrando o sistema com segurança...")
            break

        if not validar_opcao(opcao, opcoes):
            continue

        if not verificar_permissao(opcao):
            continue

        executar_opcao(opcao, opcoes)

        input("\nPressione ENTER para voltar ao menu...")