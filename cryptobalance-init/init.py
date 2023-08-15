import mysql.connector
import time

time.sleep(30)

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="1234",
    database="CryptoBalance"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE CryptoBalance (crypto VARCHAR(255), address VARCHAR(255), email VARCHAR(255), balance VARCHAR(255))")