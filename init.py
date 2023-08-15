import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="CryptoBalance"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE CryptoBalance (crypto VARCHAR(255), address VARCHAR(255), email VARCHAR(255), balance VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)