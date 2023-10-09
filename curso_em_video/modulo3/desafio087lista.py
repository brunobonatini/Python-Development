# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna = 0
maior_valor = 0

for linha in range(0, 3):
    for coluna in range (0, 3):
        matriz [linha][coluna] = int(input(f'Digite um valor para posição {linha} e {coluna}: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print(f'Soma dos pares: {soma_pares}')

for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'Soma dos valores da terceira coluna: {soma_coluna}')

for coluna in range(0, 3):
    if coluna == 0:
        maior_valor = matriz[linha][coluna]
    elif matriz[linha][coluna] > maior_valor:
        maior_valor = matriz[linha][coluna]
print(f'Maior valor da segunda linha: {maior_valor}')
    