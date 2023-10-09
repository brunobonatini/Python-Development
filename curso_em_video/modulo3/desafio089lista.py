# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota_um = float(input('Digite a primeira nota: '))
    nota_dois = float(input('Digite a segunda nota: '))
    media = (nota_um + nota_dois) / 2
    lista_alunos.append([nome, [nota_um, nota_dois], media])
    opcao = input('Deseja continuar (S/N)?: ')
    if opcao in 'Nn':
        break
print('=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('=' * 30)

for i, a in enumerate(lista_alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opcao = int(input('Mostrar a nota de qual aluno? (999 para interromper) '))
    if opcao == 999:
        print('Até a próxima.')
        break
    if opcao <= len(lista_alunos) - 1:
        print(f'Notas de {lista_alunos[opcao][0]}: {lista_alunos[opcao][1]}')