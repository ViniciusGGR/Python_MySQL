import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="123456789",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Verificando as Tabelas do banco de dados
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
