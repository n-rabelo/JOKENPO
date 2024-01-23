from random import randint, choice, shuffle
from time import sleep

print('-=' * 15)
print('\33[32mVamos Jogar Jokenpo!!!\33[m')
print('-=' * 15)
sleep(2)

itens = ('Pedra', 'Papel', 'Tesoura')
adversario = ['Ana', 'Paula', 'José', 'Heitor', 'Rafael', 'Felipe']
computador = randint(0, 2)
shuffle(adversario)
player2 = choice(adversario)

player1 = input('Qual seu nome? ').title().strip()
print(f'\nBem vindo {player1}')
print('\nSorteando adversário...')
sleep(2)
print(f'\nSeu adversário é {player2}')
sleep(2)

print('\nSuas opções: \n\033[34m[0] Pedra \n[1] Papel \n[2] Tesoura \033[m')
jogador = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 15)
print(f'O {player2} jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-=' * 15)

cont1 = 0
cont2 = 0

if computador == 0:  # player2 jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(f'{player1} VENCE')
        cont1 += 1
    elif jogador == 2:
        print(f'{player2} VENCE')
        cont2 += 1
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # player2 jogou Papel
    if jogador == 0:
        print(f'{player2} VENCE')
        cont2 += 1
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(f'{player1} VENCE')
        cont1 += 1
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # player2 jogou Tesoura
    if jogador == 0:
        print(f'{player1} VENCE')
        cont1 += 1
    elif jogador == 1:
        print(f'{player2} VENCE')
        cont2 += 1
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

print('\n')
print(f'{player1} tem {cont1} vitorias')
print(f'{player2} tem {cont2} vitorias')
