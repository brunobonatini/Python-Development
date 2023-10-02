# Faça um programa que leia 5 valores pelo teclado e guarde os em uma lista.
# Mostre qual foi o maior valor e o menor valor e sua respectivas posições na lista.

lista_valores = []
maior_valor = 0
menor_valor = 0

for i in range(0, 3):
    lista_valores.append(float(input('Digite um valor: ')))
    if i == 0:
        maior_valor = lista_valores[i]
        menor_valor = lista_valores[i]
    elif lista_valores[i] > maior_valor:
        maior_valor = lista_valores[i]
    elif lista_valores[i] < menor_valor:
        menor_valor = lista_valores[i]
        
for posicao, valor in enumerate(lista_valores):
    print(f'{posicao} : {valor}')
    
print(f'Menor valor: {menor_valor}')
print(f'Maior valor: {maior_valor}')
    