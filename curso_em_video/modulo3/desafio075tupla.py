# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
# a. Quantas vezes apareceu o valor 9; b. Em que posição foi digitado o primeiro valor 3
# c. Quais foram os números pares

valores = (int(input('Digite um número: ')), int(input('Digite um número: ')), 
           int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'{valores}')

# quantas vezes apareceu o valor 9
print(f'{valores.count(9)}')

# em qual posição apareceu o valor 3
if 3 in valores:
    print(f'{valores.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')

# quais foram os valores pares
for numero in valores:
    if numero % 2 == 0:
        print(numero)
