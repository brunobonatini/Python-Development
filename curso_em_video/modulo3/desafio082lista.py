# Crie um programa que vai ler vários valores números e colocar em uma lista.
# Crie duas listas que vão conter apenas os valores pares e os valores impares digitados respectivamente.
# Mostre o conteúdo das três listas geradas.

lista_total = []
lista_pares = []
lista_impares = []

while True:
    valores = int(input('Digite um valor: '))
    lista_total.append(valores)
    if valores % 2 == 0:
        lista_pares.append(valores)
    elif valores % 2 == 1:
        lista_impares.append(valores)
    opcao = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Lista total: {lista_total}')
print(f'Lista pares: {lista_pares}')
print(f'Lista impares: {lista_impares}')
