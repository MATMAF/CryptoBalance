# CryptoBalance
You can track your cryptocurrency balances and receive email when they change.
## Crypto supported
* Bitcoin
* Ethereum
* Dogecoin
* Litecoin
## How to use ?
### Hosted by myself
#### Comming soon at: https://cryptobalance.org
### Self hosted
Database
```docker
docker compose up -d
```
Initialize database
```python
python init.py
```
Frontend
```python
python CryptoBalance.py
```
Backend
```python
python backend.py
```

#### Replace `app.run()` with `app.run(debug=True)` at the end of the `CryptoBalance.py` file.