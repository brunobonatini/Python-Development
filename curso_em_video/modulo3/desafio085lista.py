# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for i in range(1, 8):
    valores = int(input('Digite um valor: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    if valores % 2 == 1:
        lista[1].append(valores)

lista[0].sort()
lista[1].sort()

print(f'Lista dos pares: {lista[0]}')
print(f'Lista dos ímpares: {lista[1]}')