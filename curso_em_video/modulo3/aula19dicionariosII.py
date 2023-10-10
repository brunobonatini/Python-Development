# percorrendo dicionários
pessoas = {'nome': 'leticia', 'sexo': 'F', 'idade': '25'}

for k in pessoas.keys():
    print(k)
    
for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k}: {v}')
    
# deletando um item do dicionário
del pessoas['sexo']
print(pessoas)

# alterando um valor no dicionário
pessoas['nome'] = 'laura'
print(pessoas)

# adicionando um item no dicionário
pessoas['peso'] = 70
print(pessoas)