import yfinance as yf
import pandas as pd

kodeEmiten = 'BBCA.JK'
tickerData1 = yf.Ticker(kodeEmiten)                                        
tickerDf1 = tickerData1.history() 

dataEarn = pd.DataFrame(tickerData1.earnings.T)
dataEarn.plot(kind='bar')