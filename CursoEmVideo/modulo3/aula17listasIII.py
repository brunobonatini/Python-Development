# criando uma lista
a = [2, 3, 4, 5]
b = a
b[3] = 7

# no python quando você iguala uma lista e altera uma delas, o valor altera nas 2 listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# criando uma lista
c = [5, 6, 7, 8, 9]
d = c[:]
d[2] = 10

# para não alterar o valor nas duas listas igualadas, você deve atribuir os valore de uma lista na outra utilizando :
print(f'Lista C: {c}')
print(f'Lista D: {d}')