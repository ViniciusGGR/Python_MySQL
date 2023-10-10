import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="123456789",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Criando a Tabela
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Alterando a Tabela
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
