# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre- os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. 
# Mostrar todos os valores únicos digitados em ordem crescente.

lista_valores = []

while True:
    valor = float(input('Digite um valor: '))
    if valor not in lista_valores:
        lista_valores.append(valor)
        print('Valor adicionado na lista.')
    else:
        print('Este valor já existe na lista e não será adicionado.')
    opcao = str(input('Deseja continuar (S/N)?: ')).strip().upper()[0]
    if opcao == 'N':
        break
lista_valores.sort()
print(f'Valores da lista: {lista_valores}')