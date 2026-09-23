import random

numero = random.randint(1,100)
mn = 0
print('Estou pensando em um número de 1 até 100 !\nTente adivinhar o número')
while mn!=numero:
    try:
        mn=int(input('Qual o número ? '))
        if mn<1 or mn>100 :
            print('Número inválido !\nTente um número entre 1 e 100')
        elif mn>numero:
                print(f'Você tentou {mn}')                
                print('Errado !\nTente um número menor')
        elif mn<numero:
                print(f'Você tentou {mn}')
                print('Errado !\nTente um número maior')
        elif mn == numero:
            print('Você acertou !!')
            break
    except ValueError:  print('Digite um número !')








 


