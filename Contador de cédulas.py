notas=[100, 50, 20, 10, 5, 2]
try:
    print('Digite o valor do saque:')
    saque=int(input())
    if saque<=0:
        print('Erro: O valor deve ser positivo')
    #######################################################    
    elif saque%2==0:
        for nota in notas:
            quantidade = saque // nota
            if quantidade>0:
                print(f'{quantidade} cédulas de R$ {nota}')
                saque = saque % nota
    #######################################################
    else:
        print('Erro: O valor deve ser múltiplo de 2.')
except ValueError:
    print('Erro: Digite um valor numérico vãlido.')