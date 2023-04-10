# 4.10 A cifra de Vigenère é uma variação um pouco mais segura da cifra de César
# que usa uma palavra-chave em vez de um deslocamento único 1. Começamos
# por repetir a palavra-chave (e.g., “LUAR”) ao longo do texto da mensagem; cada
# letra da chave de ‘A’ a ‘Z’ fazemos corresponder um índice de deslocamento de 0
# a 25 (e.g., “LUAR” corresponde aos deslocamentos 11, 20, 0 e 17). Assim, o texto
# “ATAQUEDEMADRUGADA” seria cifrado em “LNAHFYDVXUDIFAAUL”:

# Escreva uma função vigenere(chave,txt) que implemente esta cifra.
