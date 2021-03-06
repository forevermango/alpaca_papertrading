import requests 
import json
from config import *



BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)

#response = create_order("AAPL", 100, "buy", "market", "gtc")
#response = create_order("GME", 1000, "buy", "market", "gtc")
#orders = get_orders()
#print(response)
#print(orders)

data = {
    "symbol": "AAPL",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "gtc",
    "take-profit": {
        "limit_price": "140"
    }, 
    "stop_loss": {
        "stop_price": "135",
#can take off for day trades
        "limit_price": "130"
    }
}

r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

response = json.loads(r.content)

print(response)