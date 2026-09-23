import os
from funcoes import contar_porcentagem

valor= float(input('Qual o valor da conta ? '))
porcentagem= float(input('Qual a porcentagem da gorjeta ? '))

total, gorjeta = contar_porcentagem(valor, porcentagem)

print(f'O valor da gorjeta é: R${gorjeta}\nO valor total é de: R${total}')
input()
