# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

notas = {}

notas['nome'] = str(input('Digite o nome do aluno: '))
notas['media:'] = float(input('Digite a média do aluno: '))

for c, v in notas.items():
    print(f'{c}: {v}')