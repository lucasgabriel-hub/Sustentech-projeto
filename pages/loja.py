"""
Loja de recompensas — troca de tokens por benefícios.
"""

from services.token_service import TokenService
from utils.utilidades import UI

"""
Itens disponíveis na loja. Cada item tem um ID, nome e preço em tokens.
"""
ITENS_LOJA = [
    {"id": 1, "nome": "Ficha do RU",                    "preco": 25},
    {"id": 2, "nome": "Ticket Cinema",                  "preco": 60},
    {"id": 3, "nome": "Cupom de Desconto em Lojas",     "preco": 90},
    {"id": 4, "nome": "Desconto Assinatura Xbox",       "preco": 150},
]


def tela_loja(conexao, usuario_id: int) -> None:
    """
    Exibe a tela da loja de recompensas, permitindo que o usuário resgate itens usando seus tokens.
    """
    token_service = TokenService(conexao)

    while True:
        UI.limpar()
        UI.cabecalho("Loja de Recompensas 🛒")

        saldo = token_service.saldo(usuario_id)
        print(f"💰 Seu saldo: {saldo} tokens")
        UI.separador()

        print("Itens disponíveis:\n")
        for item in ITENS_LOJA:
            print(f"  {item['id']}. {item['nome']:<35} {item['preco']} tokens")

        UI.separador()
        print("  0. Voltar ao menu principal")
        UI.separador()

        opcao = input("Escolha o número do item que deseja resgatar: ").strip()

        if opcao == "0":
            UI.limpar()
            break

        # Para validar se a opção corresponde a um item
        item_escolhido = next(
            (i for i in ITENS_LOJA if str(i["id"]) == opcao), None
        )

        if item_escolhido is None:
            UI.erro("Opção inválida. Tente novamente.")
            UI.pausar()
            continue

        # Verifica saldo
        if saldo < item_escolhido["preco"]:
            faltam = item_escolhido["preco"] - saldo
            UI.erro(
                f"Tokens insuficientes! Você possui {saldo} tokens, "
                f"mas precisa de {item_escolhido['preco']}. "
                f"Faltam {faltam} tokens."
            )
            UI.pausar()
            continue

        # Confirmação antes de resgatar
        confirmado = UI.confirmar(
            f"Resgatar '{item_escolhido['nome']}' por {item_escolhido['preco']} tokens?"
        )
        if not confirmado:
            print("Resgate cancelado.")
            UI.pausar()
            continue

        # Deduz os tokens (registra com quantidade negativa)
        conexao.execute(
            """
            INSERT INTO tokens (usuario_id, meta_id, quantidade, descricao)
            VALUES (?, 0, ?, ?)
            """,
            (
                usuario_id,
                -item_escolhido["preco"],
                f"Resgate na loja: {item_escolhido['nome']}",
            ),
        )
        conexao.commit()

        UI.sucesso(
            f"'{item_escolhido['nome']}' resgatado com sucesso! "
            f"Novo saldo: {saldo - item_escolhido['preco']} tokens 🎉"
        )
        UI.pausar()