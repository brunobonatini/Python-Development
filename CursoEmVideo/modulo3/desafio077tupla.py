# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Mostre, para cada palavra, quais são suas vogais

palavras = ("casa", "carro", "chave", "gato", "livro")

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')