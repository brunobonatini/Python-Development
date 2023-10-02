# Crie um programa que leia o ano de nascimento de sete pessoas.
# Mostre quantas pessoas não atingiram a maior idade e quantas já são maiores.
# Considere a maior idade 21 anos.

# importando a biblioteca para datas
from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor = 0

for i in range(1, 8):
    nascimento = int(input('Qual ano a pessoa {} nasceu: '.format(i)))
    idade = ano_atual - nascimento

    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Total de pessoas maiores de idade: {total_maior}')
print(f'Total de pessoas menores de idade: {total_menor}')
        