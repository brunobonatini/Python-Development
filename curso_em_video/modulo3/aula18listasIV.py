'''
lista = []
lista.append('Bruno')
lista.append(30)
print(lista)

pessoas = []
pessoas.append(lista[:])
print(pessoas)

lista[0] = 'Leticia'
lista[1] = 20

pessoas.append(lista[:])
print(pessoas[]) 
'''
pessoas = [['Bruno', 30], ['Leticia', 25], ['Laura', 15], ['Ozzy', 5]]
for p in pessoas:
    print(f'Nome: {p[0]} - Idade: {p[1]}')

frutas = []
sacola = []


