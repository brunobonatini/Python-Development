# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla
# Mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Valores sorteados: ', end='')
for n in num:
    print(f'{n} ', end='')
    
# maior valor sorteado
print(f'\nMaior valor sorteado: {max(num)}')
print(f'Menor valor sorteado: {min(num)}')
