

from configuration import *

import datetime
import pickle
import warnings

from hmmlearn.hmm import GaussianHMM
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import numpy as np
import pandas as pd
import seaborn as sns


client = bitmex.bitmex(
    test = IS_TEST,
    api_key = API_KEY,
    api_secret = API_SECRET
)

prices = pd.DataFrame(client.Trade.Trade_getBucketed(
    binSize='1d',
    symbol='XBTUSD',
    count=1000,
    reverse=True,
).result()[0])

prices.set_index(['timestamp'], inplace=True)
prices = prices.sort_values(by='timestamp', ascending=True)

rets=np.column_stack([prices['close'].pct_change()])
rets[0]=0

hmm_model = GaussianHMM(
    n_components=2, covariance_type="full", n_iter=10
).fit(rets)

print("Model Score:", hmm_model.score(rets))

hmm_model.predict(rets)

hmm_model.predict(rets2)[-1]