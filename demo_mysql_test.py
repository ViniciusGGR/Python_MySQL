import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="123456789"
)

mycursor = mydb.cursor()

# Criando um banco de dados
# mycursor.execute("CREATE DATABASE mydatabase")

# Verificando os bancos de dados
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
