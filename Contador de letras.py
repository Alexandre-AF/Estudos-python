from funcoes import contar_palavras

frase = input('Digite uma frase: ').strip()
if not frase:
    print('Erro: Nenhuma frase foi digitada.')
else:
    resultado = contar_palavras(frase)
    if resultado:
        print('Contagem de palavras: ')
        for palavras, quantidade in resultado.items():
            print(f'{palavras}:{quantidade}')
    else:
        print(f'Nenhuma palavra válida foi encontrada.')

