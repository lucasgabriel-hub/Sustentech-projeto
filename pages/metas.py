"""Tela de metas sustentáveis."""

from models.meta import TipoMeta
from services.meta_service import MetaService
from services.token_service import TokenService
from utils.utilidades import UI


def tela_metas(conexao, usuario_id: int) -> None:
    """
    Exibe a tela de metas sustentáveis para o usuário.
    """
    service = MetaService(conexao)
    token_service = TokenService(conexao)

    while True:
        saldo = token_service.saldo(usuario_id)
        UI.cabecalho("Metas Sustentáveis")
        print(f"  🪙 Seu saldo de tokens: {saldo}")
        UI.separador()
        print("1. Metas Diárias")
        print("2. Metas Semanais")
        print("3. Metas Mensais")
        print("4. Histórico de tokens")
        print("5. Voltar ao menu principal")
        UI.separador()

        opcao = input("Escolha uma aba: ").strip()

        mapa = {"1": TipoMeta.DIARIA, "2": TipoMeta.SEMANAL, "3": TipoMeta.MENSAL}

        if opcao in mapa:
            UI.limpar()
            _menu_tipo(service, usuario_id, mapa[opcao])
        elif opcao == "4":
            UI.limpar()
            _exibir_historico_tokens(token_service, usuario_id)
        elif opcao == "5":
            UI.limpar()
            break
        else:
            UI.erro("Opção inválida.")
            UI.pausar()


def _menu_tipo(service: MetaService, usuario_id: int, tipo: TipoMeta) -> None:
    """
    Exibe o menu de metas para um tipo específico (diária, semanal ou mensal).
    """
    while True:
        UI.cabecalho(f"Metas {tipo.value.upper()}")
        print("1. Ver metas")
        print("2. Concluir uma meta")
        print("0. Voltar")
        UI.separador()

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            UI.limpar()
            _exibir_metas(service, usuario_id, tipo)
        elif opcao == "2":
            UI.limpar()
            _concluir_meta(service, usuario_id, tipo)
        elif opcao == "0":
            UI.limpar()
            break
        else:
            UI.erro("Opção inválida.")
            UI.limpar()


def _exibir_metas(service: MetaService, usuario_id: int, tipo: TipoMeta) -> list:
    """
    Exibe as metas de um tipo específico e retorna a lista de metas.
    """
    from models.token import TOKENS_POR_TIPO
    metas = service.listar(usuario_id, tipo)
    tokens_val = TOKENS_POR_TIPO.get(tipo, 0)

    UI.cabecalho(f"📊 Metas {tipo.value.upper()} — vale {tokens_val} 🪙 cada")
    for i, meta in enumerate(metas, start=1):
        print(f"{i}. {meta.descricao}")
        print(f"   Status: {meta.icone_status()} {meta.status.value}")
        UI.separador()

    return metas


def _concluir_meta(service: MetaService, usuario_id: int, tipo: TipoMeta) -> None:
    """
    Permite ao usuário concluir uma meta e ganhar tokens.
    """
    metas = _exibir_metas(service, usuario_id, tipo)
    if not metas:
        UI.aviso("Nenhuma meta encontrada.")
        UI.pausar()
        return

    try:
        opcao = int(input("Número da meta a concluir: "))
        if not (1 <= opcao <= len(metas)):
            UI.erro("Número inválido.")
            return

        meta_escolhida = metas[opcao - 1]
        sucesso, mensagem, tokens = service.concluir(meta_escolhida, usuario_id)
        print(mensagem)

        if sucesso and tokens > 0:
            from services.token_service import TokenService
            from database.connection import conectar_banco
            # saldo já atualizado — mostramos inline
            pass

    except ValueError:
        UI.erro("Entrada inválida. Digite um número.")

    UI.pausar("Pressione Enter para voltar:")
    UI.limpar()


def _exibir_historico_tokens(token_service: TokenService, usuario_id: int) -> None:
    """
    Exibe o histórico de tokens ganhos pelo usuário.
    """
    saldo = token_service.saldo(usuario_id)
    historico = token_service.historico(usuario_id, limite=10)

    UI.cabecalho("🪙 Histórico de Tokens")
    print(f"  Saldo total: {saldo} token(s)\n")

    if not historico:
        UI.aviso("Nenhum token ganho ainda. Conclua metas para acumular!")
    else:
        for entrada in historico:
            print(f"  {entrada}")

    UI.separador()
    UI.pausar()
    UI.limpar()
