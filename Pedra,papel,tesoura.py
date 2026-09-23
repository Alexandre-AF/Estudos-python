import random

jogada=['pedra','papel','tesoura']

print('Faça a sua escolha:\nPedra \nPapel \nTesoura')
eu=input()
pc=random.choice(jogada)

if eu not in jogada:
    print(f'Suajogada inválida !!\nEntre com uma jogada válida')
elif eu=='pedra' and pc=='pedra':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nEmpate !')
elif eu=='pedra'and pc=='papel':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê perdeu !')
elif eu=='pedra' and pc=='tesoura':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê ganhou !')

elif eu=='papel' and pc=='papel':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nEmpate !')
elif eu=='papel'and pc=='tesoura':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê perdeu !')
elif eu=='papel' and pc=='pedra':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê ganhou !')

elif eu=='tesoura' and pc=='tesoura':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nEmpate !')
elif eu=='tesoura'and pc=='pedra':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê perdeu !')
elif eu=='tesoura' and pc=='papel':
    print(f'Sua jogada foi {eu}\nE a do seu adversário foi {pc}\nVocê ganhou !')
