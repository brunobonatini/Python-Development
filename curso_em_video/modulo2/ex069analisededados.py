# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

'''maior_idade = 0
homens = 0
mulheres_menores = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    opcao = input('Deseja continuar (S/N)? ').strip().upper()[0]
    if idade > 18:
        maior_idade += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres_menores += 1
    if opcao == 'N':
        break
print(f'Total de pessoal com mais de 18 anos: {maior_idade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menores}')'''

maior_idade = 0
homens = 0
mulheres_menores = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]

    if idade > 18:
        maior_idade += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres_menores += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar o cadastro (S/N)? ')
                    ).strip().upper()[0]
    if opcao == 'N':
        break

print(f'Total de pessoal com mais de 18 anos: {maior_idade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menores}')
print('Cadastro finalizado.')
