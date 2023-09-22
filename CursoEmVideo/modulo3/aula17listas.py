lista = [2, 5, 9, 1]
print(lista)

# alterando valores em uma lista
lista[2] = 3
print(lista)

# adicionando valores em uma lista
lista.append(7)
print(lista)

# inserindo valores em uma posição na lista
lista.insert(1, 9)
print(lista)

# ordenando uma lista em ordem crescente
lista.sort()
print(lista)

# ordenando uma lista em ordem decrescente
lista.sort(reverse=True)
print(lista)

# removendo o último elemento da lista
lista.pop()
print(lista)

# removendo um elemento passando sua posição na lista
lista.pop(3)
print(lista)

# adicionando um valor repetido na lista
lista.append(7)
print(lista)

# removendo um elemento da lista com *remove
lista.remove(7)
print(lista)

if 5 in lista:
    lista.remove(5)
else:
    print('O número 4 não está na lista')
print(lista)

# mostrando o tamanho da lista
print(f'{len(lista)}')