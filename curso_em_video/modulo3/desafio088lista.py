# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('=' * 30)
print(' ' * 9, 'Mega Sena')
print('=' * 30)

lista_total = []
lista_jogos = []
quantidade_jogos = int(input('Digite a quantidade de jogos a serem sorteados: '))
total_jogos = 1

while total_jogos <= quantidade_jogos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista_total:
            lista_total.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista_total.sort()
    lista_jogos.append(lista_total[:])
    lista_total.clear()
    total_jogos += 1
print(f'Sorteando {quantidade_jogos} jogos')

for i, l in enumerate(lista_jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
