# Crie um programa que leia uma frase qualquer.
# Diga se ela é um palindromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer: ')).strip().upper()

palavras = frase.split()
juntar_palavras = ''.join(palavras)
inverter_palavra = juntar_palavras[::-1] # do inicio ao final de trás para frente

print(f'{juntar_palavras}')
print(f'{inverter_palavra}')

if inverter_palavra == juntar_palavras:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
