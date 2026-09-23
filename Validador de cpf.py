try:
    cpf=int(input('Digite seu cpf: '))
    if len(str(cpf)) == 11:
        print('CPF válido')
    else:
        print('CPF inválido')
except ValueError:
    print('Erro: O CPF deve conter apenas números !!')