import emoji
from random import randint
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
adversario = ('Ana', 'Paula', 'José', 'Heitor', 'Rafael', 'Felipe')
computador = randint(0, 2)
player2 = randint(0, 4)

player1 = input('Qual seu nome? ')
print(f'Bem vindo {player1}')
print('Sorteando adversário...')
sleep(2)
print(f'Seu adversário é {adversario[player2]}')
sleep(2)
print('\nVamos Jogar!!!')
sleep(2)
print(emoji.emojize('\nSuas opções: \n[0] Pedra :raised_fist:\n[1] Papel :raised_hand:\n[2] Tesoura :victory_hand:'))
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print(f'O {adversario[player2]} jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-=' * 15)

cont1 = 0
cont2 = 0

if computador == 0:  # computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(emoji.emojize(f'{player1} VENCE :partying_face:'))
        cont1 += 1
    elif jogador == 2:
        print(emoji.emojize(f'{adversario[player2]} VENCE :partying_face:'))
        cont2 += 1
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # computador jogou Papel
    if jogador == 0:
        print(emoji.emojize(f'{adversario[player2]} VENCE :partying_face:'))
        cont2 += 1
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(emoji.emojize(f'{player1} VENCE :partying_face:'))
        cont1 += 1
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou Tesoura
    if jogador == 0:
        print(emoji.emojize(f'{player1} VENCE :partying_face:'))
        cont1 += 1
    elif jogador == 1:
        print(emoji.emojize(f'{adversario[player2]} VENCE :partying_face:'))
        cont2 += 1
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

print('\n')
print(f'{player1} tem {cont1} vitorias')
print(f'{adversario[player2]} tem {cont2} vitorias')
