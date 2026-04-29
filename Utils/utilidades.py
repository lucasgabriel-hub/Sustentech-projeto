"""Funções auxiliares reutilizáveis."""
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
    print("\n" * 50)

def tamanho(texto):
    if len(texto) < 3 or len(texto) > 20:
        return False
    return True
    