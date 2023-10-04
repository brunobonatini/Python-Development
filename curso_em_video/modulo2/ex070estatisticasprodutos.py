# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_compra = 0
produto_acima_1000 = 0
menor_preco = 0
cont = 0
nome_produto_barato = ' '

while True:
    nome_produto = input('Write the product name: ')
    preco_produto = float(input('Write the product price: '))
    cont += 1
    total_compra += preco_produto

    if preco_produto > 1000.0:
        produto_acima_1000 += 1
    if cont == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_produto_barato = nome_produto

    option = ' '
    while option not in 'YN':
        option = str(
            input('Do you want continue the register (Y/N)? ')).strip().upper()[0]
    if option == 'N':
        break
print('End register')
print(f'Total da compra: {total_compra:.2f}')
print(f'Produtos acima de 1000.0: {produto_acima_1000}')
print(f'Nome do produto mais barato: {nome_produto_barato}')
