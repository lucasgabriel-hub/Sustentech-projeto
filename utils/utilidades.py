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
    