
#importar o random para implementar o número oculto
import random
def space():
    print('\n' * 10)

#Aqui é  linha de código que armazena o número oculto entre 1 e 30
numero = random.randint(1,30)

#Criar uma lista para armazenar os números digitados pelo jogador
lista = list()

nome = input('Olá, primeiro me diga o seu nome:')




print(f'''Bem vindo ao Jogo de Adivinhação,  {nome}!
Primeiro vamos as regras: Você terá 10 chances de acertar o número oculto e a cada tentativa eu digo se o número é maior ou menor
OK, lá vou eu
=====JOGO DO ADVINHA=====''')
tentativa = 11
#Aqui se inicia o loop (coloquei tentativa >2 porque  a ultima tentativa, que é o 2, não conseguir arrumar sem colocar em um novo while
while tentativa >2:
    chute = int(input('{}, agora digite uma número de 1 a 30:'.format(nome)))
    # Dentro do while, criar as condicionais "if", para verificar tanto se o número digitado já se encontra na lista
    # quanto para comparar o número digitado com o número oculto
    if chute in lista:
        print('==========')
        print('Esse número já foi digitado, tente outro')
        print('Essa é sua lista de números digitados: {}'.format((lista)))
        print('Esse é o seu número de tentativas restantes: {}'.format(tentativa-1))
        print('==========')
    elif chute == numero:
       print('Parabéns {}, você acertou! Você é fera nos jogos de advinhação!'.format(nome))
       lista.append(chute)
       #Lista.sort(), para colocar os números adicionados na lista em ordem, para após isso, printar ao usuário
       lista.sort()
     #===============
       #O break para quebrar o loop e continuar o código
       break
    elif chute > numero:
       tentativa = tentativa-1
       print('==========')
       print('OPS! Número errado, tente um menor')
       lista.append(chute)
       lista.sort()
       print('Essa é a sua lista de números digitados:{}'.format((lista)))
       print('Esse é o seu número de tentativas restantes: {}'.format(tentativa - 1))
       print('==========')
    elif chute < numero:
       tentativa = tentativa-1
       lista.append(chute)
       lista.sort()
       print('==========')
       print('OPS! Número errado, tente um maior')
       print('Essa é a sua lista de números digitados:{}'.format((lista)))
       print('Esse é o seu número de tentativas restantes: {}'.format(tentativa - 1))
       print('=========')
        #Como ainda não tenho muito conhecimento, tive que fazer a ultima tentativa em um "while" separado,
        #pois mostrava na tela frases indesejadas. Mesmo quando acabava as tentativas do jogador,
        #Aparecia a mensagem de que era para o jogador digitar mais um número
while tentativa == 2:
        chute = int(input('{}, agora digite um número de 1 a 30:'.format(nome)))
        if chute in lista:
          print('==========')
          print('Esse número já foi digitado, tente outro')
          print('Essa é sua lista de números digitados: {}'.format((lista)))
          print('Esse é o seu número de tentativas restantes: {}'.format(tentativa - 1))
          print('==========')
        elif chute == numero:
            print('==========')
            print('Parabéns {}, você acertou! Você é fera nos jogos de advinhação!'.format(nome))
            lista.append(chute)
            lista.sort()
            print('==========')
            break
        elif chute != numero:
            print('Que pena,{},  você perdeu...'.format(nome))
            lista.append(chute)
            lista.sort()
            print('==========')
            break
#bloco de código usado para mostrar o maior e menor número da lista de números digitados
ultimo_lista = lista[-1]
print('O maior número digitado foi: {}'.format(ultimo_lista))
primeiro_lista = lista[0]
print("O menor número digitado foi: {}".format(primeiro_lista))
print('=====FIM DE JOGO!=====')

