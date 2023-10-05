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
sacola_frutas = []

for i in range(1, 5):
    frutas.append(input('Fruta: '))
    frutas.append(float(input('Preço: ')))
    sacola_frutas.append(frutas[:])
    frutas.clear()
print(f'Sacola de frutas: {sacola_frutas}')
