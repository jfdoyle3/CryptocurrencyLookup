import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="python-sandbox"
)


print(mydb)