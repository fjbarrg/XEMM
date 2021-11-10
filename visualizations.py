
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: visualizations.py                                                                             -- #
# -- Description: Functions for plots, tables and text visualizations for the project                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/IFFranciscoME/MarketMaker-BackTest                                   -- #
# --------------------------------------------------------------------------------------------------------- #

# -- Load base packages
import pandas as pd
from plotly.subplots import make_subplots

import plotly.graph_objects as go

def graficas(df, symbol):
    # separamos el DataFrame por exchanges
    df_f = df[df.exchange== 'ftx']
    df_c = df[df.exchange == 'currencycom']
    df_k = df[df.exchange == 'kraken']
    df_b =df[df.exchange == 'bitfinex']
    #generamos subplots
    fig = make_subplots(rows=2, cols=3,
    subplot_titles=('levels', 'ask_vol', 'bid_vol', 'total_vol', 'mid_price', 'vwap'))
    
    #gráfica 1: levels
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.level, mode='lines', name='ftx level'),row=1, col=1)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.level,mode='lines', name='currencycom level'),row=1,col=1)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.level,mode='lines', name='kraken level'),row=1,col=1)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.level,mode='lines', name='bitfinex level'),row=1,col=1)
    
    #gráfica 2: ask_vol
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.ask_vol, mode='lines', name='ftx ask_vol'),row=1, col=2)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.ask_vol,mode='lines', name='currencycom ask_vol'),row=1,col=2)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.ask_vol,mode='lines', name='kraken ask_vol'),row=1,col=2)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.ask_vol,mode='lines', name='bitfinex ask_vol'),row=1,col=2)

    #gráfica 3:bid_vol
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.bid_vol, mode='lines', name='ftxbid_vol'),row=1, col=3)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.bid_vol,mode='lines', name='currencycom bid_vol'),row=1,col=3)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.bid_vol,mode='lines', name='kraken bid_vol'),row=1,col=3)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.bid_vol,mode='lines', name='bitfinex bid_vol'),row=1,col=3)

    #gráfica 4:total_vol
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.total_vol, mode='lines', name='ftx total_vol'),row=2, col=1)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.total_vol,mode='lines', name='currencycom total_vol'),row=2,col=1)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.total_vol,mode='lines', name='kraken total_vol'),row=2,col=1)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.total_vol,mode='lines', name='bitfinex total_vol'),row=2,col=1)

    #gráfica 5: mid_price
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.mid_price, mode='lines', name='ftx mid_price'),row=2, col=2)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.mid_price,mode='lines', name='currencycom mid_price'),row=2,col=2)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.mid_price,mode='lines', name='kraken mid_price'),row=2,col=2)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.mid_price,mode='lines', name='bitfinex mid_price'),row=2,col=2)

    #gráfica 6:vwap
    fig.add_trace(go.Scatter(x=df_f.timeStamp, y=df_f.vwap, mode='lines', name='ftx vwap'),row=2, col=3)
    fig.add_trace(go.Scatter(x=df_c.timeStamp, y=df_c.vwap,mode='lines', name='currencycom vwap'),row=2,col=3)
    fig.add_trace(go.Scatter(x=df_k.timeStamp, y=df_k.vwap,mode='lines', name='kraken vwap'),row=2,col=3)
    fig.add_trace(go.Scatter(x=df_b.timeStamp, y=df_b.vwap,mode='lines', name='bitfinex vwap'),row=2,col=3)
    
    return fig.show()