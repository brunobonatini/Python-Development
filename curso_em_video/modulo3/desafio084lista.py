# Faça um programa que leia nome e peso de 3 pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
for i in range(1, 4):
    nome = input(f'Digite o nome da {i}ª pessoa: ')
    pessoas.append(nome)
    peso = int(input(f'Digite o peso da {i}ª pessoa: '))
    pessoas.append(peso)
print(f'{pessoas}')