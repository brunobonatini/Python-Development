# Faça um programa que leia nome e peso de 3 pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = []
pessoas = []
pessoa_mais_pesada = 0
pessoa_mais_leve = 0

for i in range(1, 4):
    lista.append(input(f'Digite o nome da {i}ª pessoa: '))
    lista.append(int(input(f'Digite o peso da {i}ª pessoa: ')))
    if len(pessoas) == 0:
        pessoa_mais_pesada = lista[1]
        pessoa_mais_leve = lista[1]
    else:
        if lista[1] > pessoa_mais_pesada:
            pessoa_mais_pesada = lista[1]
        if lista[1] < pessoa_mais_leve:
            pessoa_mais_leve = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    
print(f'Lista de pessoas: {pessoas}')
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso: {pessoa_mais_pesada}kg')
print(f'Menor peso: {pessoa_mais_leve}kg')

for p in pessoas:
    if p[1] == pessoa_mais_pesada:
        print(f'Pessoa mais pesada: [{p[0]}]')
    elif p[1] == pessoa_mais_leve:
        print(f'Pessoa mais leve: [{p[0]}]')  