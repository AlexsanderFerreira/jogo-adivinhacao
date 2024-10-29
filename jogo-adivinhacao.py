# jogo da adivinhação
from random import randint

print('###############################################')
print('Bem vindo ao jogo da adivinhação usando while!')
print('###############################################')

print('\n')

n_secreto = randint(1, 5)
n_escolhido = 0

while True:
    n_escolhido = int(input('Escolha um número de 1 a 5: '))

    if n_escolhido not in (1, 2, 3, 4, 5):
        print('Número precisa estar entre 1 e 5!')
        continue
    elif n_escolhido == n_secreto:
        print(f'Parabéns! Você acertou o número secreto: {n_secreto}!')
        break
    else:
        print('Você errou!')