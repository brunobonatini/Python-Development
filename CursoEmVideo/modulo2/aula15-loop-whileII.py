'''cont = 1
while cont <=10:
    print(cont, '...', end='')
    cont += 1
print('Fim')'''

numero = 0
soma = 0

while numero != 10:
    numero = int(input('Digite um número: '))
    soma += numero
print(f'Soma: {soma}') # o valor 10 que seria para sair do loop, entra na soma


numero = 0
soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 10:
        break
    soma += numero
print(f'Soma: {soma}')