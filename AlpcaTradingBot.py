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

    #determines when positions are heald and how long tghey are held for 
    def rebalance(self):
        tRerank = threading.Thread(target=self.rerank)
        tRerank.start()
        tRerank.join()

        #clear positions
        orders = self.alpaca.list.orders(status="open")
        for order in orders:
            self.alpacha.cancel_order(order.id)

        print("taking long position in" + str(self.long))
        print("taking short position in" + str(self.long))

        #Remove posiions that are no longer in the short or long list, 
        # and make a list of positions that do not need to change. 
        #Adjust quantities if needed, 
        executed = [[], []]
        positions = self.alpaca.list_positions()
        self.blacklist.clear()
        for position in positions:
            if(self.long.count(positions.symbol) == 0):
                #position not in short list
            if(self.short.count(positions.symbol) == 0):
                #clear position if not in either long of short
                if (position.side == "long"):
                    side = "sell"
                else: 
                    side = "buy"
                respSP = []
                tSO = threading.Thread(target=self.submitOrder, 
                ergs=[abs(int(float(position.qty))),
                positions.symbol, side, resSO])
                tSO.start()
                tSO.join()
                else: 
                    if(positions.side == "long"):
                        side = "sell"
                        respSO = []
                        tSO = threading.Thread(target=self.submitOrder),
                            args=[int(float(position.qty)),
                        position.symbol, side, respSO])
                        tSO.start()
                        tSO.join()
                    else: 
                        if(abd(int(float(position.qty))) == self.qShort):
                            #Position is where we want it. Pass for now
                        pass
                    else: 
                        diff = abs(int(float(positions.qty))) - self.qShort
                        if(diff > 0):
                            side = "buy"
                        else: 
                            side = "sell"
                        respSO = []
                        tSP = threading.Thread
                        (target=self.submitOrder, args=[abs(diff), position.symbol, side, respSO])
                        tSO.start()
                        tSO.join()
                    executed[10.append(position.symbol)
                    self.blacklist.add(position.symbol)
                else: 

    

















