import alpaca_trade_api as tradeapi

api = tradeapi.REST()
account = api.get_account()
account.status