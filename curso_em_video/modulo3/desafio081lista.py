# Crie um programa que vai ler vários números e colocar em uma lista.
# a. Quantos numeros foram digitados b. A lista de valores ordenada de forma decrescente
# c. Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont += 1
    opcao = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if opcao == 'N':
        break
    
lista.sort(reverse=True)        
print(f'Lista {lista}')
print(f'Quantidade de valores na lista: {cont}')

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O numero 5 não esta na lista.')
