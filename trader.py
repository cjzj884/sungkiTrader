import datetime
import telepot
import pandas as pd

class Trader():
    def __init__(self, client, strategy, money_to_trade = 10, leverage = 1):
        self.client = client
        self.strategy = strategy
        self.money_to_trade = money_to_trade
        self.leverage = leverage

    def execute_trade(self):

        tele_token = '964075190:AAHERFIxiQK9Z0dER9xKfzyOIcOcVTmiYjo'
        tele_bot = telepot.Bot(tele_token)

        tele_result = {1: '숏 포지션 청산',
                       -1: '롱 포지션 청산',
                       2: '숏 포지션 청산 후 롱 포지션 진입',
                       -2: '롱 포지션 청산 후 숏 포지션 진입',
                       3: '롱 포지션 진입',
                       -3: '숏 포지션 진입',
                       0: 'no signal'
                       }

        prediction = self.strategy.predict()


