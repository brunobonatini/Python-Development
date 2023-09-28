# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
maior_valor = 0
menor_valor = 0

while True:
    numero = int(input('Digite um valor: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior_valor = menor_valor = numero
    elif numero > maior_valor:
        maior_valor = numero
    elif numero < menor_valor:
        menor_valor = numero       
     
    resposta = input('Deseja continuar (S/N)? ').lower().strip()[0]
    if resposta != 's':
        break
media = soma / cont       
print(f'Quantidade de valores digitados: {cont}')
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media:.2f}')
print(f'Maior valor digitado: {maior_valor}')
print(f'Menor valor digitado: {menor_valor}')