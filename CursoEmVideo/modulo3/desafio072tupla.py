# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20
# Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
         'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Você digitou um número invalido. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número válido: ')
        
print(f'O número {num} por extenso é: {numeros[num]}')

# Quer continuar?