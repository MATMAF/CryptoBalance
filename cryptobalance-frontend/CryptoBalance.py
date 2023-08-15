from flask import Flask, request, render_template, redirect, url_for
from flask_sslify import SSLify
import mysql.connector
import time

time.sleep(60)

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="1234",
    database="CryptoBalance"
)
mycursor = mydb.cursor()

def EnterSQL(crypto, address, email):
    sql = "INSERT INTO CryptoBalance (crypto, address, email) VALUES (%s, %s, %s)"
    val = (crypto, address, email)
    mycursor.execute(sql, val)
    mydb.commit()

def DeleteSQL(address):
    mycursor.execute(f"DELETE FROM CryptoBalance WHERE address = '{address}'")
    mydb.commit()

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

@app.route('/tracker/submit', methods=['POST'])
def add():
    crypto = request.form['crypto']
    address = request.form['address']
    email = request.form['email']
    EnterSQL(crypto, address.lower(), email)
    return redirect(url_for('index'))

@app.route('/remove_tracker')
def remove_tracker():
    return render_template('remove_tracker.html')

@app.route('/remove_tracker/submit', methods=['POST'])
def remove():
    address = request.form['address']
    DeleteSQL(address.lower())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')