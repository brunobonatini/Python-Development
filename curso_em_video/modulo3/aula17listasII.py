# criando uma lista em branco
numeros = []

# adicionando valores na lista
numeros.append(1)
numeros.append(2)
numeros.append(3)

for n in numeros:
    print(f'{n}')
    
# adicionando valores pelo teclado
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))

for posicao, numero in enumerate(numeros):
    print(f'Posição {posicao} - Valor: {numero}')

print(f'{numeros}')