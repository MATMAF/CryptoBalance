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

btc_address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
balance = get_btc_balance(btc_address)

if balance is not None:
    print(f"BTC balance of address {btc_address}: {balance} BTC")