def limpar_texto(texto):
    texto = texto.lower()
    caracteres = "!@#$%¨&*()_+{}[];:,.<>?/\|"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavras in palavras:
        contagem[palavras] = contagem.get(palavras,0) + 1
    return contagem

def contar_porcentagem(valor, porcentagem):
    gorjeta = valor * (porcentagem / 100)
    total = valor + gorjeta
     
    return total, gorjeta

def contar_vogais(frase):
    vogais= 'aeiou'
    contador = 0
    for letra in frase:
        if letra.lower() in vogais:
            contador += 1
    return contador

def soma(a,b):
    resultado=a+b
    return resultado

def subtracao(a,b):
    resultado=a-b
    return resultado

def multiplicacao(a,b):
    resultado=a*b
    return resultado

def divisao(a,b):
    resultado=a/b
    return resultado

def calculadora():
    try:
        num_1 = float(input('Qual o primeiro número ? '))
        print('Qual a operação ? (+, -, *, /)')
        cond = input()
        num_2 = float(input('Qual o segundo número ? '))

        if cond=='+':
            resultado=soma(num_1,num_2)
            print(f' {num_1:>7g}')
            print(f'+{num_2:>7g}')
            print(' '+ '-' *7)
            print(f' {resultado:>7g}')
        elif cond=='-':
            resultado=subtracao(num_1,num_2)
            print(f' {num_1:>7g}')
            print(f'-{num_2:>7g}')
            print(' '+ '-' *7)
            print(f' {resultado:>7g}')
        elif cond=='*':
            resultado=multiplicacao(num_1,num_2)
            print(f' {num_1:>7g}')
            print(f'*{num_2:>7g}')
            print(' '+ '-' *7)
            print(f' {resultado:>7g}')
        elif cond=='/':
            resultado=divisao(num_1,num_2)
            print(f' {num_1:>7g}')
            print(f'/{num_2:>7g}')
            print(' '+ '-' *7)
            print(f' {resultado:>7g}')
        else:
            print('Erro !!\nOperação inválida !')
        
    except ZeroDivisionError:
        print('Erro !!\nNão é possível dividir por zero !')

    except ValueError:
        print('Erro !!\nDigite somente números !')        


