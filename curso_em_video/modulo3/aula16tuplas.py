lanche = ('hamburger', 'churrasco', 'pizza', 'hot-dog', 'batata-frita')

'''print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Vou comprar {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
    
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print('Comi todos os itens do cardápio')

# mostrando a tupla ordenada
print(sorted(lanche))

tupla_a = (2, 5, 8)
tupla_b = (3, 6, 9, 7)
tupla_c = tupla_a + tupla_b

print(tupla_a)
print(tupla_b)
print(tupla_c)
print(len(tupla_c))
print(tupla_c.count(5))
print(tupla_c.index(8))'''

# dados diferentes em tuplas
pessoa = ('Bruno', 36, 'M', 1.70)

#podemos apagar uma tupla, mas não podemos apagar um item de uma tupla
del(pessoa)
print(pessoa)