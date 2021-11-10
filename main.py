
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: main.py                                                                                       -- #
# -- Description: Main execution logic for the project                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/IFFranciscoME/MarketMaker-BackTest                                   -- #
# --------------------------------------------------------------------------------------------------------- #

# -- Load Packages for this script
import pandas as pd
import numpy as np

import nest_asyncio
nest_asyncio.apply()

# -- Load other scripts
from data import fees_schedule, order_book

# Massive download of OrderBook data

def dict_data(symbol):
    exchanges =["ftx","currencycom","bitfinex","kraken","coinmate"] 
    
    data = order_book(symbol=symbol, exchanges=exchanges, output='inplace', stop=None, verbose=True)
    #data = order_book(symbol='BTC/USD', exchanges=exchanges, output='inplace', stop=None, verbose=True)
    
    dict ={}

    for exchange in exchanges:
        for i in range(len(list(data[exchange].keys()))):
            tmp = data[exchange][list(data[exchange].keys())[i]]
            fechas=list(data[exchange].keys())
            llave = "ocurrencia_" + str(i+1)
            dict[llave] = {'timeStamp':fechas[i],
                    'exchange': exchange, 
                    'level' : len(tmp),
                    'ask_vol' :  tmp.ask_size.sum(),
                    'bid_vol' : tmp.bid_size.sum(),
                    'total_vol' : tmp.ask_size.sum() + tmp.bid_size.sum(),
                    'mid_price' :  (tmp.ask_size.sum() + tmp.bid_size.sum()).mean(),
                    'vwap' : ((tmp.bid_size.sum()*tmp.bid)/tmp.bid_size.sum() + (tmp.ask_size.sum()*tmp.ask)/tmp.bid_size.sum()).mean()
                            } 
     
    return pd.DataFrame(dict).T    

    df.exchange.unique()       
        
# Test
# data['kraken'][list(data['kraken'].keys())[2]]

# Read previously downloaded file
ob_data = pd.read_json('files/orderbooks_06jun2021.json', orient='values', typ='series')

# -- Simulation of trades (Pending)

"""
- Type A: Make a BID in Kraken, then Take BID in Bitfinex

Check Signal_BID
    Difference between BIDs on Origin and Destination is greater than Maker_Margin_BID
    Make on Destination and Take on Origin

kr_maker_bid * (1 + kr_maker_fee) = bf_taker_bid * (1 - bf_taker_fee)
e.g. -> 5942.5638 * (1 + 0.0016) = 5964.00 * (1 - 0.0020) = 0

- Type B: Take an ASK on Bitfinex, then Make an ASK in Kraken

Check Signal_ASK
    Difference between ASKs on Origin and Destination is greater than Maker_Margin_ASK
    Take on Origin and Maker on Destination

bf_taker_ask * (1 + bf_taker_fee) = kr_maker_ask * (1 - kr_maker_fee)
e.g. -> 6000 * (1 + 0.0020) - 6021.6346 * (1 - 0.0016) = 0
"""
