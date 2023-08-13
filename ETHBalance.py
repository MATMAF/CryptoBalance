import requests
import config

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

eth_address = "0xCD7468def591FCeBe99DCA6A34caB0AcFf46c882"
eth_api_key = config.ETH_API

balance = get_eth_balance(eth_address, eth_api_key)

if balance is not None:
    print(f"ETH balance of address {eth_address}: {balance} ETH")