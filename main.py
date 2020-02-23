import bitmex
import time

from configuration import *

client = bitmex.bitmex(
    test = IS_TEST,
    api_key = API_KEY,
    api_secret = API_SECRET
)

