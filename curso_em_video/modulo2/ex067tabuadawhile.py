# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero_tabuada = int(input('Digite um número para saber sua tabuada: '))
    if numero_tabuada < 0:
        break
    for num in range(1, 11):
        print(f'{numero_tabuada} x {num} = {numero_tabuada * num}')
print('Programa encerrado.')
