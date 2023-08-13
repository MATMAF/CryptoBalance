import requests
import config
import CryptoCheck
import time

def ChangeBalanceCryptoCheck(balance):
    with open('CryptoCheck.py', 'r') as file:
        lines = file.readlines()
    new_value = balance
    for i, line in enumerate(lines):
        if 'BALANCE' in line:
            lines[i] = f'BALANCE = "{new_value}"\n'
    with open('CryptoCheck.py', 'w') as file:
        file.writelines(lines)

def get_btc_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_satoshis = int(response.text)
        balance_btc = balance_satoshis / 10**8
        return balance_btc
    else:
        return None
    
def get_eth_balance(address, api_key):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_wei = int(response.json()['result'])
        balance_eth = balance_wei / 10**18
        return balance_eth
    else:
        return None
    
def get_crypto_to_usd_exchange_rate(crypto):
    if crypto == "BTC":
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            btc_to_usd_rate = data.get("bitcoin", {}).get("usd", 0)
            return btc_to_usd_rate
        else:
            return None

    elif crypto == "ETH":
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            btc_to_usd_rate = data.get("ethereum", {}).get("usd", 0)
            return btc_to_usd_rate
        else:
            return None
    
    else:
        return None

CryptoCheck_balance = CryptoCheck.BALANCE

while True:

    if CryptoCheck.CRYPTO == "BTC":
        while True:
            btc_balance = get_btc_balance(CryptoCheck.ADDRESS)
            if btc_balance == CryptoCheck_balance:
                time.sleep(150)
            else:
                exchange_rate = get_crypto_to_usd_exchange_rate(CryptoCheck.CRYPTO)
                usd_balance = btc_balance * exchange_rate
                sender_name = "CryptoBalance"
                receiver_email = CryptoCheck.EMAIL
                subject = f"Your {CryptoCheck.CRYPTO} balance"
                message = f"BTC balance of address {CryptoCheck.ADDRESS}: {btc_balance} BTC\nEquivalent balance in USD: {usd_balance:.2f} USD\n\nPowered by @MATMAF\nhttps://www.mat.run"
                SendMail = requests.get(f"https://mail.mat.run/api?name={sender_name}&receiver={receiver_email}&sub={subject}&message={message}")
                ChangeBalanceCryptoCheck(btc_balance)
                CryptoCheck_balance = btc_balance
    
    if CryptoCheck.CRYPTO == "ETH":
        while True:
            eth_balance = get_eth_balance(CryptoCheck.ADDRESS, config.ETH_API)
            if eth_balance == CryptoCheck_balance:
                time.sleep(150)
            else:
                exchange_rate = get_crypto_to_usd_exchange_rate(CryptoCheck.CRYPTO)
                usd_balance = eth_balance * exchange_rate
                sender_name = "CryptoBalance"
                receiver_email = CryptoCheck.EMAIL
                subject = f"Your {CryptoCheck.CRYPTO} balance"
                message = f"ETH balance of address {CryptoCheck.ADDRESS}: {eth_balance} ETH\nEquivalent balance in USD: {usd_balance:.2f} USD\n\nPowered by @MATMAF\nhttps://www.mat.run"
                SendMail = requests.get(f"https://mail.mat.run/api?name={sender_name}&receiver={receiver_email}&sub={subject}&message={message}")
                ChangeBalanceCryptoCheck(eth_balance)
                CryptoCheck_balance = eth_balance