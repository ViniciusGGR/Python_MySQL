import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="123456789",
    database="mydatabase"
)