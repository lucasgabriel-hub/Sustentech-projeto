"""Funções auxiliares reutilizáveis."""
import os
"""
pacotes de emojis para deixar a interface mais amigavel
"""
emojis = {
    '✅': '✅',
    '❌': '❌',
    '🔴': '🔴',
    '🟢': '🟢',
    '🎯': '🎯',
    '🌱': '🌱',
    '⚠️': '⚠️',
    '♻️': '♻️',
    '🎉': '🎉',
    '📊': '📊',
    '💡': '💡',
    '🚨': '🚨',
    '👥': '👥',
    }

def limpar_tela():
    #print("\n"* 50")
    os.system('cls' if os.name == 'nt' else 'clear')

def tamanho(texto):
    if len(texto) < 3 or len(texto) > 20:
        return False
    return True

def confirmarsaidarecomendacao():
    while True:
        resposta = input('Deseja sair da seção de recomendações? ("sim" ou "não"): ')
        if resposta == 'sim':
            return True
        elif resposta == 'não':
            return False
        else:
            print('Resposta invalida. Por favor, responda com "sim" ou "não".')
    