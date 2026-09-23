tarefas=['Regar as plantas']

while True:
    print('*' *13)
    print(' Gerenciador\n     de\n   tarefas ')
    print('*' *13)

    print('Olá!!\nEscolha uma opção:\n1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefas\n4. Sair')
    op=int(input())

    if op==1:
        print('Adicionar tarefa: ')
        print('Digite a tarefa a ser adicionada: ')
        task=input().strip()
        tarefas.append(task)
        print('Tarefa adicionada com sucesso!')
        input()
    elif op==2:
        print('Visualizador de tarefas: ')
        for tarefa in tarefas:
            print(f'- {tarefa}')
        input()
    elif op==3:
        print('Removedor de tarefas')
        print('Qual tarefas deve ser retirada ?')
        for tarefa in tarefas:
                    print(f'- {tarefa}')
        remove=input()
        if remove not in tarefas:
            print('Tarefa inexistente!')
            input()
        else :
            tarefas.remove(remove)
            print('Tarefa removida com sucesso!')
            input()
    elif op==4:
        print('Até logo!')
        break
    else:
        print('Opção inválida!')
        input()
