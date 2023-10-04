# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre em uma lista,
# na posição correta de inserção sem usar o sort(). Mostre a lista ordenada na tela.

lista_valores = []

for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0 or n > lista_valores[-1]:
        lista_valores.append(valor)
    else:
        posicao = 0
        while posicao < len(lista_valores):
            if valor <= lista_valores[posicao]:
                lista_valores.insert(posicao, valor)
                break
            posicao += 1
print(lista_valores)

'''
lis = [ ]
for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1 or n >= lis[-1]:
        lis.append(n)
    elif n <= lis[0]:
        lis.insert(0, n)
    elif lis[0] <= n <= lis[1]:
        lis.insert(1, n)
    elif lis[1] <= n <= lis[2]:
        lis.insert(2, n)
    elif lis[2] <= n <= lis[3]:
        lis.insert(3, n)
print(lis)
'''
