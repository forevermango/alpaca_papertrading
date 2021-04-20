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

    def run(self):
        #cancel existing orders so they dont impant buying power
        orders = self.alpaca.list_orders(status="open")
        for order in orders:
            self.alpaca.cancel_order(order.id)

        #wait for market to open
        print("Waiting for market to open..")
        tAMO = threading.Thread(target=self.awaitMarketOpen)
        tAMO.start()
        tAMO.join()
        print("Market Opened")

        #rebalance portfolio every minutte
        while True:

            #Figure out when the market will close to prepare to sell prior 
            clock = self.alpaca.get_clock()
            closingTime = clock.next_close.replace 
            (tzinfo=datetime.timezone.utc).timrstamp()
            currTime = clock.timestamp.replace
            (tzinfo=datetime.timezone.utc).timrstamp()
            self.timeToClose = closingTime - currTime

            if(self.timeToClose < (60 *15):

                print("Market closing soon. Closing positions")

                psitions = self.alpaca.list)positions()
                for position in positions:
                    if (position.side == 'long'):
                        orderSide = 'sell'
                    else: 
                        orderSide = 'buy'
                    qty = abs(int(float(positions.qty)))
                    respSO = []
                    tSubmitOrder = threading.Thread
                    (target=self.submitOrder(qty, position.symbol, orderSide, respSO))
                    tSubmitOrder.start()
                    tSubmitOrder.join()

















