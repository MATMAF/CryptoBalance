import mysql.connector
import requests
import time

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="CryptoBalance"
)
mycursor = mydb.cursor()

def EditSQL(address, balance):
    mycursor.execute(f"UPDATE CryptoBalance SET balance = '{balance}' WHERE address = '{address}'")
    mydb.commit()

def GetSQL():
    mycursor.execute("SELECT crypto, address, email, balance FROM CryptoBalance")
    return mycursor.fetchall()

def get_balance(crypto, address):
    if crypto == "BTC":
        url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_satoshis = int(data["data"][address]["address"]["balance"])
        balance_btc = f"{balance_satoshis / 10**8}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_btc, balance_usd
    elif crypto == "ETH":
        url = f"https://api.blockchair.com/ethereum/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_wei = int(data["data"][address]["address"]["balance"])
        balance_eth = f"{balance_wei / 10**18}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_eth, balance_usd
    elif crypto == "DOGE":
        url = f"https://api.blockchair.com/dogecoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_doge = data["data"][address]["address"]["balance"]
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_doge, balance_usd
    elif crypto == "LTC":
        url = f"https://api.blockchair.com/litecoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_litoshi = int(data["data"][address]["address"]["balance"])
        balance_ltc = f"{balance_litoshi / 10**8}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_ltc, balance_usd
    else:
        return None, None

while True:
    mydb.reconnect()

    users = GetSQL()

    for row in users:
        crypto, address, email, balance = row
        current_balance = get_balance(crypto, address)
        if current_balance[0] is None or current_balance[1] is None:
            pass
        elif current_balance[0] != balance:
            sender_name = "CryptoBalance"
            receiver_email = email
            subject = f"Your {crypto} balance"
            message = f"{crypto} balance of address {address}: {current_balance[0]} {crypto}\nEquivalent to: {current_balance[1]:.2f} USD\nhttps://www.cryptobalance.dev\n\nPowered by @MATMAF\nhttps://www.mat.run"
            SendMail = requests.get(f"https://mail.mat.run/api?name={sender_name}&receiver={receiver_email}&sub={subject}&message={message}")
            EditSQL(address, current_balance[0])

    time.sleep(30)
