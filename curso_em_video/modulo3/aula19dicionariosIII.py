# criando dicionários dentro de listas
estado_um = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado_dois = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil = []

brasil.append(estado_um)
brasil.append(estado_dois)

print(brasil[1]['uf'])
print(brasil[0]['sigla'])

# adicionando itens pelo teclado
estado = {}
pais = []
for e in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    pais.append(estado.copy())
for e in pais:
    for c, v in e.items():
        print(f'{c} - {v}')