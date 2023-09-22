# Faça um programam que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

PESO_MAIOR = 0
PESO_MENOR = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))  
    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'Peso maior: {peso_maior}')
print(f'Peso menor: {peso_menor}')
