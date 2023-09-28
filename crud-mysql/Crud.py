# importando a biblioteca para a conexão com o banco de dados
import mysql.connector

# criando a conexão com o bando de dados
conection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'db_tecstart'
)

# instanciando a conexão
newConection = conection.cursor()

"""# inserindo dados no banco de dados
insert = 'INSERT INTO tbl_cliente (nome, cpf, email, telefone, idade) VALUES ("Bruno", "12345678901", "btcstart@gmail.com", "999887766", 30)'

newConection.execute(insert)
conection.commit()

# fechando a conexão com o banco
newConection.close()
conection.close()

# inserindo dados no banco de dados
nomeCliente = "Laura"
cpfCliente = "14725836987"
emailCliente = "lauratecstart@gmail.com"
telCliente = "988887755"
idadeCliente = 20

insert = f'INSERT INTO tbl_cliente (nome, cpf, email, telefone, idade) VALUES ("{nomeCliente}","{cpfCliente}","{emailCliente}","{telCliente}","{idadeCliente}")'

newConection.execute(insert)
conection.commit()

newConection.close()
conection.close()

# Atualizando um dado no banco de dados
nomeCliente = "Bruno"
idadeCliente = 25

updateIdade = f'UPDATE tbl_cliente SET idade = "{idadeCliente}" WHERE nome = "{nomeCliente}"'

newConection.execute(updateIdade)
conection.commit()

newConection.close()
conection.close()

# deletando um dado do banco de dados
nomeCliente = "Laura"

deleteCliente = f'DELETE FROM tbl_cliente WHERE nome = "{nomeCliente}"'

newConection.execute(deleteCliente)
conection.commit()

# inserindo dados no banco de dados
nomeCliente = "Laura"
cpfCliente = "14725836987"
emailCliente = "lauratecstart@gmail.com"
telCliente = "988887755"
idadeCliente = 20

insertCliente = f'INSERT INTO tbl_cliente (nome, cpf, email, telefone, idade) VALUES ("{nomeCliente}","{cpfCliente}","{emailCliente}","{telCliente}","{idadeCliente}")'

newConection.execute(insertCliente)
conection.commit()

# Consultando no banco de dados
consultSelect = 'SELECT * FROM tbl_cliente'

newConection.execute(consultSelect)

retorno = newConection.fetchall()

print(retorno)

newConection.close()
conection.close()

# deletando um dado do banco de dados
idCliente = 4

deleteCliente = f'DELETE FROM tbl_cliente WHERE id_cliente = "{idCliente}"'

newConection.execute(deleteCliente)
conection.commit()

newConection.close()
conection.close()
"""
# Retornando a consulta ordenada por nome
consultSelect = f'SELECT * FROM tbl_cliente ORDER BY nome'

newConection.execute(consultSelect)

retorno = newConection.fetchall()
print(retorno)

newConection.close()
conection.close()

# Filtrando a consulta por nome
nomeCliente = "Bruno"

consultSelect = f'SELECT * FROM tbl_cliente WHERE nome = "{nomeCliente}"'

newConection.execute(consultSelect)

retorno = newConection.fetchall()
print(retorno)

newConection.close()
conection.close()