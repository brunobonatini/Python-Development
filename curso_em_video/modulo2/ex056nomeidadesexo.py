# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# Mostre:
# A média de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos.

SOMA_IDADE = 0
MEDIA_IDADE = 0
MULHERES = 0
NOME_HOMEM_VELHO = ''
IDADE_HOMEM_VELHO = 0

for p in range(1, 5):
    nome = input(f'Digite o nome da {p}ª pessoa: ').strip()
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo = input(f'Digite o sexo da {p}ª pessoa (M/F): ').strip()
    SOMA_IDADE += idade
    if p == 1 and sexo in 'Mn':
        NOME_HOMEM_VELHO = nome
        IDADE_HOMEM_VELHO = idade
    if sexo in 'Mn' and idade > IDADE_HOMEM_VELHO:
        IDADE_HOMEM_VELHO = idade
        NOME_HOMEM_VELHO = nome
    if sexo in 'Ff' and idade < 20:
        MULHERES += 1
media_idade = SOMA_IDADE / 4
print(f'Média de idade do grupo: {media_idade} anos')
print(f'Homem mais velho: {NOME_HOMEM_VELHO}')
print(f'Idade do {NOME_HOMEM_VELHO}: {IDADE_HOMEM_VELHO} anos')
print(f'Quantidade de mulheres com menos de 20 anos: {MULHERES}')
