# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços.
# Mostre uma listagem de preços organizando os dados em forma tabular.

lista_escolar = ('Lapis', 1.75, 'Borracha', 2.00, 'Caneta', 7.90, 'Caderno', 15.90, 'Mochila', 97.90, 'Estojo', 21.90)

print('-' * 40)
print(f'{"Lista Escolar":^40}')
print('-' * 40)

for posicao in range(0, len(lista_escolar)):
    if posicao % 2 == 0:
        print(f'{lista_escolar[posicao]:.<30}', end='')
    else:
        print(f'R${lista_escolar[posicao]:>6.2f}')
print('-' * 40)