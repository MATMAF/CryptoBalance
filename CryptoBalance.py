import requests

def get_btc_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_satoshis = int(response.text)
        balance_btc = balance_satoshis / 10**8
        return balance_btc
    else:
        print("Error fetching balance.")
        return None
    
def get_eth_balance(address, api_key):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_wei = int(response.json()['result'])
        balance_eth = balance_wei / 10**18
        return balance_eth
    else:
        print("Error fetching balance.")
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
            print("Error fetching exchange rate.")
            return None

    elif crypto == "ETH":
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            btc_to_usd_rate = data.get("ethereum", {}).get("usd", 0)
            return btc_to_usd_rate
        else:
            print("Error fetching exchange rate.")
            return None
    
    else:
        print("Error your crypto isn't supported yet.")
        return None