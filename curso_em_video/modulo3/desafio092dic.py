# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
dados['nome'] = input('Digite o nome do funcionário: ')
nascimento = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Digite o número da carteira de trabalho (0 para sair): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
else:
    print('Carteira de trabalho não cadastrada.')

print(dados)
