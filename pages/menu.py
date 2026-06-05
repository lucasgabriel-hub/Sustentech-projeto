"""Menu principal do Sustentech."""

from models.usuario import Usuario
from database.connection import conectar_banco
from pages.Dicas import tela_dicas
from pages.metas import tela_metas
from pages.recomendacoes import tela_recomendacoes
from pages.usuarios import tela_usuarios
from pages.quiz import tela_quiz
from pages.mapadescarte import rotas_descarte
from pages.loja import tela_loja
from utils.utilidades import UI


def menu_principal(conexao, usuario: Usuario) -> None:
    """
    Exibe o menu principal do Sustentech.
    """
    conexao = conectar_banco()

    while True:
        UI.cabecalho("Menu Principal")
        print(usuario.saudacao())
        UI.separador()
        print("1. Dicas")
        print("2. Metas")
        print("3. Quiz")
        print("4. Recomendações")
        print("5. Usuários")
        print("6. Loja")
        print("7. Rotas de Descarte")
        print("8. Sair")
        UI.separador()

        opcao = input("Escolha uma opção: ").strip()

        acoes = {
            "1": lambda: tela_dicas(),
            "2": lambda: tela_metas(conexao, usuario.id),
            "3": lambda: tela_quiz(),
            "4": lambda: tela_recomendacoes(),
            "6": lambda: tela_loja(conexao, usuario.id),
            "7": lambda: rotas_descarte(),
        }

        if opcao in acoes:
            UI.limpar()
            acoes[opcao]()

        elif opcao == "5":
            UI.limpar()
            conta_deletada = tela_usuarios(conexao, usuario.id)
            if conta_deletada:
                print("Até logo! Sua conta foi removida. 🌱")
                conexao.close()
                return

        elif opcao == "8":
            print("Saindo... Até logo! 🌱")
            conexao.close()
            break

        else:
            UI.erro("Opção inválida.")
            UI.limpar()
