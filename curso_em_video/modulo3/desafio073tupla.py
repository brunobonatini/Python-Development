# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro na ordem de colocação.
# Mostre: a. Apenas os 5 primeiros colocados b. Os últimos 4 colocados da tabela c. Uma lista com os times em orgem alfabética.
# d. Em que posição na tabela está o time do Santos

tabela_brasileiro = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo', 'Fluminense', 'Fortaleza', 
         'Atlético-PR', 'Atlético-MG', 'Cruzeiro', 'Cuiabá', 'Internacional', 'São Paulo', 
         'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'América-MG', 'Coritiba')

print('***' * 20)
print("************** Classificação do Brasileirão ****************")
print('***' * 20)

# a. Os 5 primeiros colocados
print(f'\nPrimeiros 5 colocados: {tabela_brasileiro[:5]}')

# b. Os 4 últimos colocados
print(f'\nRebaixados: {tabela_brasileiro[-4:]}')

# c. os times por ordem alfabética
print(f'\nLista de times: {sorted(tabela_brasileiro)}')

# d. posição do Santos na tabela
time_procurado = "Santos"
if time_procurado in tabela_brasileiro:
    posicao = tabela_brasileiro.index(time_procurado) + 1
    print(f'\nO time do {time_procurado} está na {posicao}ª posição da tabela.')
else:
    print(f'\nO time do {time_procurado} não está na tabela deste ano.\n')
    
print('***' * 20)
print()

# classificação do campeonato
for posicao, tabela_brasileiro in enumerate(tabela_brasileiro, start=1):
    print(f'{posicao}: {tabela_brasileiro}')