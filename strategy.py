import pandas as pd

class Strategy():
    def __init__(self, client, timeframe = '30s', stoploss = 0.3, profitreal = 1):
        self.client = client
        self.timeframe = timeframe
        self.stoploss = stoploss
        self.profitreal = profitreal

    def predict(self):

