# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0
derrotas = 0

while True:
    jogador = int(input('Digite um valor para Par ou Impar: '))
    computador = randint(0, 10)
    total = jogador + computador
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = input('Par ou Impar (P/I)? ').strip().upper()[0]
    print(f'Jogador = {jogador} - Computador = {computador}', end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')

    if par_impar == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif par_impar == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')

print(f'Vitórias: {vitorias}')
print(f'Derrotas: {derrotas}')
