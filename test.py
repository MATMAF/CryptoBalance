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

def get_btc_to_usd_exchange_rate():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        btc_to_usd_rate = data.get("bitcoin", {}).get("usd", 0)
        return btc_to_usd_rate
    else:
        print("Error fetching exchange rate.")
        return None

btc_address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
balance_btc = get_btc_balance(btc_address)
if balance_btc is not None:
    exchange_rate = get_btc_to_usd_exchange_rate()
    if exchange_rate is not None:
        balance_usd = balance_btc * exchange_rate
        print(f"BTC balance of address {btc_address}: {balance_btc} BTC")
        print(f"Equivalent balance in USD: {balance_usd:.2f} USD")
