import requests
import config
import time

def ChangeBalanceConfig(balance):
    with open('config.py', 'r') as file:
        lines = file.readlines()
    new_value = balance
    for i, line in enumerate(lines):
        if 'BALANCE' in line:
            lines[i] = f'BALANCE = "{new_value}"\n'
    with open('config.py', 'w') as file:
        file.writelines(lines)

def get_balance(crypto, address):
    if crypto == "BTC":
        url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_satoshis = int(data["data"][address]["address"]["balance"])
        balance_btc = f"{balance_satoshis / 10**8}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_btc, balance_usd
    if crypto == "ETH":
        url = f"https://api.blockchair.com/ethereum/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_wei = int(data["data"][address]["address"]["balance"])
        balance_eth = f"{balance_wei / 10**18}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_eth, balance_usd
    if crypto == "DOGE":
        url = f"https://api.blockchair.com/dogecoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_doge = data["data"][address]["address"]["balance"]
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_doge, balance_usd
    if crypto == "LTC":
        url = f"https://api.blockchair.com/litecoin/dashboards/address/{address}"
        response = requests.get(url)
        data = response.json()
        balance_litoshi = int(data["data"][address]["address"]["balance"])
        balance_ltc = f"{balance_litoshi / 10**8}"
        balance_usd = data["data"][address]["address"]["balance_usd"]
        return balance_ltc, balance_usd

config_crypto = config.CRYPTO
config_address = config.ADDRESS
config_balance = config.BALANCE

while True:
    balance = get_balance(config_crypto, config_address)

    if balance[0] == config_balance:
        time.sleep(150)
    else:
        sender_name = "CryptoBalance"
        receiver_email = config.EMAIL
        subject = f"Your {config_crypto} balance"
        message = f"{config_crypto} balance of address {config_address}: {balance[0]} {config_crypto}\nEquivalent to: {balance[1]:.2f} USD\n\nPowered by @MATMAF\nhttps://www.mat.run"
        SendMail = requests.get(f"https://mail.mat.run/api?name={sender_name}&receiver={receiver_email}&sub={subject}&message={message}")
        ChangeBalanceConfig(balance[0])
        config_balance = balance[0]
        time.sleep(30)