import os
from funcoes import contar_vogais

texto=input('Digite um texto: ')
contador= contar_vogais(texto)

print(f'O texto digitado possui {contador} vogais.')
input()
os.system('cls')