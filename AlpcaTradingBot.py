import alpaca-trade-api as tradeapi
import threading 
import timeimport datetime
from config import *


BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

class LongShort:
    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, ACCOUNT_URL)

        stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GME'. 'SNAP', 'SHOP', 'SPLK',
        'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'BA', 'TWLO', 'MS', 'BAC',]
        self.allStocks = []
        for stock in stockUniverse: 
            self.allStocks.append([stock, 0])

        self.long = []
        self.short = []
        self.qShort = None
        self.qlong = None
        self.adjustedQLong = None
        self.adjuctedqShort = None
        self.blacklist = set()
        self.longAmount = 0
        self.shortAmount = 0
        self.timeToClose = None

        

