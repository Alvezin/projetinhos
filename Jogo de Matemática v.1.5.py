from random import randint

def somaJog_1(Range1: int, Range2: int):
    acerto = 0
    erro = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        soma = num1 + num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}+{num2}? ' + '\033[0;0m'))
        if result == soma:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto += 1
        elif result != soma:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro += 1
        print('\n' * 50)
    return acerto


def somaJog_2(Range1: int, Range2: int):
    acerto1 = 0
    erro1 = 0
    acerto2 = 0
    erro2 = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        input(f'{nome1}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        soma = num1 + num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}+{num2}? ' + '\033[0;0m'))
        if result == soma:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto1 += 1
        elif result != soma:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro1 += 1
        print('\n' * 50)

        input(f'{nome2}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        soma = num1 + num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}+{num2}? ' + '\033[0;0m'))
        if result == soma:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto2 += 1
        elif result != soma:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro2 += 1
        print('\n' * 50)
    return acerto1, acerto2


def multJog_1(Range1: int, Range2: int):
    acerto = 0
    erro = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        mult = num1 * num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}X{num2}? ' + '\033[0;0m'))
        if result == mult:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto += 1
        elif result != mult:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro += 1
        print('\n' * 50)
    return acerto


def multJog2(Range1: int, Range2: int):
    acerto1 = 0
    erro1 = 0
    acerto2 = 0
    erro2 = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        input(f'{nome1}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        mult = num1 * num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}X{num2}? ' + '\033[0;0m'))
        if result == mult:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto1 += 1
        elif result != mult:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro1 += 1
        print('\n' * 50)

        input(f'{nome2}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range1, Range2)
        mult = num1 * num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}X{num2}? ' + '\033[0;0m'))
        if result == mult:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto2 += 1
        elif result != mult:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro2 += 1
        print('\n' * 50)
    return acerto1, acerto2


def subJog1(Range1: int, Range2: int, Range3: int):
    acerto = 0
    erro = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range3, Range1)
        sub = num1 - num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}-{num2}? ' + '\033[0;0m'))
        if result == sub:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto += 1
        elif result != sub:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro += 1
        print('\n' * 50)
    return acerto


def subJog2(Range1: int, Range2: int, Range3: int):
    acerto1 = 0
    erro1 = 0
    acerto2 = 0
    erro2 = 0
    sit = 0
    for player in range(0, 10):
        sit += 1
        input(f'{nome1}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range3, Range1)
        sub = num1 - num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}-{num2}? ' + '\033[0;0m'))
        if result == sub:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto1 += 1
        elif result != sub:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro1 += 1
        print('\n' * 50)

        input(f'{nome2}, vamos lá (aperte ENTER...)')
        print('Pergunta N°', sit)
        num1 = randint(Range1, Range2)
        num2 = randint(Range3, Range1)
        sub = num1 - num2
        result = int(input('\033[32m' + f'Qual o resultado para: {num1}-{num2}? ' + '\033[0;0m'))
        if result == sub:
            input('\033[32m' + f'Parabéns, você é fera!!!' + '\033[0;0m')
            acerto2 += 1
        elif result != sub:
            input('\033[32m' + 'Ops! Número errado, veja se acerta a próxima' + '\033[0;0m')
            erro2 += 1
        print('\n' * 50)
    return acerto1, acerto2


if __name__ == '__main__':

    print('\n' * 20)

    num_jogador = int(input('Número de Jogadores (1-2) : '))
    if num_jogador == 1:
        nome1 = input('Olá, matemático, pronto para iniciar? Diga-me seu nome: ')
    elif num_jogador == 2:
        print('Olá matemáticos, vamos iniciar?')
        nome1 = input('Jogador 1, digite seu nome: ')
        nome2 = input('Jogador 2, diga seu nome: ')

        input(f'Ok, {nome1} e {nome2}, farei 10 perguntas de matemática, conforme a escolha de vocês... ')

    print('\n' * 20)

    escolha = int(input('\033[31m' + f'''Selecione o tipo de operação? 
                        (1) Soma
                        (2) Multiplicação
                        (3) Subtração
    ''' + '\033[0;0m'))

    dificuldade = int(input('''Selecione o  nível de dificuldade?
                        (1) Fácil
                        (2) Médio
                        (3) Díficil
    '''))

    print('\n' * 20)
    if num_jogador == 1:
        if escolha == 1:
            if dificuldade == 1:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {somaJog_1(1,10)} ACERTOS''')
            elif dificuldade == 2:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {somaJog_1(10, 100)} ACERTOS''')
            elif dificuldade == 3:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {somaJog_1(100, 1000)} ACERTOS''')
        elif escolha == 2:
            if dificuldade == 1:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {multJog_1(1,10)} ACERTOS''')
            elif dificuldade == 2:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {multJog_1(10, 50)} ACERTOS''')
            elif dificuldade == 3:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {multJog_1(50, 100)} ACERTOS''')
        elif escolha == 3:
            if dificuldade == 1:
                print(f'''PLACAR DE ACERTOS: \n'
                      {nome1} --- {subJog1(50, 100, 0)} ACERTOS''')
            elif dificuldade == 2:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {subJog1(100,200,0)} ACERTOS''')
            elif dificuldade == 3:
                print(f'''PLACAR DE ACERTOS: 
                      {nome1} --- {subJog1(1000,3000,100)} ACERTOS''')
    elif num_jogador == 2:
        if escolha == 1:
            if dificuldade == 1:
                print(f'''          PLACAR DE ACERTOS: 
                                          
                       {nome1} --> {somaJog_2(1,10)} <-- {nome2} ''')
            elif dificuldade == 2:
                print(f'''          PLACAR DE ACERTOS: 

                        {nome1} --> {somaJog_2(10, 100)} <-- {nome2} ''')
            elif dificuldade == 3:
                print(f'''          PLACAR DE ACERTOS: 

                        {nome1} --> {somaJog_2(100, 1000)} <-- {nome2} ''')
        elif escolha == 2:
            if dificuldade == 1:
                print(f'''          PLACAR DE ACERTOS: 

                        {nome1} --> {multJog2(1, 10)} <-- {nome2} ''')
            elif dificuldade == 2:
                print(f'''          PLACAR DE ACERTOS: 

                        {nome1} --> {multJog2(10, 50)} <-- {nome2} ''')
            elif dificuldade == 3:
                print(f'''          PLACAR DE ACERTOS: 

                        {nome1} --> {multJog2(50, 100)} <-- {nome2} ''')
        elif escolha == 3:
            if dificuldade == 1:
                print(f'''          PLACAR DE ACERTOS: 

                            {nome1} --> {subJog2(50, 100, 0)} <-- {nome2} ''')
            elif dificuldade == 2:
                print(f'''          PLACAR DE ACERTOS: 

                            {nome1} --> {subJog2(100, 200, 0)} <-- {nome2} ''')
            elif dificuldade == 3:
                print(f'''          PLACAR DE ACERTOS: 

                            {nome1} --> {subJog2(1000, 3000, 100)} <-- {nome2} ''')
