# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[], [], []]

for i in range(1, 4):
    valores1 = int(input('Digite um valor: '))
    matriz[0].append(valores1)

for i in range(1, 4):
    valores2 = int(input('Digite um valor: '))
    matriz[1].append(valores2)

for i in range(1, 4):
    valores3 = int(input('Digite um valor: '))
    matriz[2].append(valores3)

print(matriz)
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha} e {coluna}: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
