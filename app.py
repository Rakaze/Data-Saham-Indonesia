import streamlit as st
import pandas_datareader as web
import yfinance as yf
import pandas as pd
import datetime
from googletrans import Translator
import plotly.graph_objects as go
from numerize import numerize


st.set_page_config(page_title='Aplikasi Data Saham Indonesia', layout="wide", page_icon='🤑')
translator = Translator()

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
footer{
    visibility:hidden;
}
footer:after{
    content:'Made with ❤ by Raka Luthfi';
    display:block;
    position:relative;
    color:white;

}

"""

st.sidebar.subheader('Masukkan Kode Emiten ')
kodeEmiten = st.sidebar.text_input('Kode Emiten', 'BBCA.JK')
data_period = st.sidebar.selectbox('Periode', ('1d', '3d', '1wk', '1mo', '3mo'))
data_interval = st.sidebar.radio('Interval', ['15m', '30m', '1h', '1d', '5d'])

st.write('''

# Data Saham 📈

Menampilkan data saham Indonesia

''')
st.write('---')

col1, col2 = st.columns(2)
with col1:
    col1.header('Grafik IHSG')
    data = yf.download(tickers='^JKSE', period='6mo', interval='1d')
    config = {'displayModeBar': False}
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                        open=data['Open'],
                                        high=data['High'],
                                        low=data['Low'],
                                        close=data['Close']
                                        )])
    fig.update_layout(xaxis_rangeslider_visible=False, xaxis_fixedrange=True, yaxis_fixedrange=True)
    col1.plotly_chart(fig, use_container_width=True, config=config)

with col2:
    col2.header('Data IHSG Hari Ini')
    tickIHSG = '^JKSE'
    dataIHSG = yf.Ticker(tickIHSG)
    hargaIHSG = dataIHSG.history(period='1d')
    estimasi = round(hargaIHSG, 3)
    kenaikan = (estimasi['Close'][0] - estimasi['Open'][0])
    kenaikan = round(kenaikan, 3)

    col2.metric("Harga", estimasi['Close'][0], kenaikan)
    col2.metric('Volume Transaksi', hargaIHSG['Volume'][0])
    tertinggi = round(hargaIHSG['High'][0], 3)
    col2.metric('Tertinggi', tertinggi)
    terendah = round(hargaIHSG['Low'][0], 3)
    col2.metric('Terendah', terendah)

st.write('---')
st.write("### Trending")
col3, col4, col5, col6 = st.columns(4)
with col3:
    bbca_tick = 'BBCA.JK'
    bbca = yf.Ticker(bbca_tick)
    bbca_1d = bbca.history(period='1d')
    bbca_per = bbca_1d['Close'][0] - bbca_1d['Open'][0]
    bbca_per = round(bbca_per, 3)
    col3.metric("BBCA", bbca_1d['Close'], bbca_per)

with col4:
    tlkm_tick = 'TLKM.JK'
    tlkm = yf.Ticker(tlkm_tick)
    tlkm_1d = tlkm.history(period='1d')
    tlkm_per = tlkm_1d['Close'][0] - tlkm_1d['Open'][0]
    tlkm_per = round(tlkm_per, 3)
    col4.metric("TLKM", tlkm_1d['Close'], tlkm_per)

with col5:
    asii_tick = 'ASII.JK'
    asii = yf.Ticker(asii_tick)
    asii_1d = asii.history(period='1d')
    asii_per = (asii_1d['Close'][0] - asii_1d['Open'][0])
    asii_per = round(asii_per, 3)
    col5.metric("ASII", asii_1d['Close'], asii_per)

with col6:
    unvr_tick = 'UNVR.JK'
    unvr = yf.Ticker(unvr_tick)
    unvr_1d = unvr.history(period='1d')
    unvr_per = unvr_1d['Close'][0] - unvr_1d['Open'][0]
    unvr_per = round(unvr_per, 3)
    col6.metric("UNVR", unvr_1d['Close'], unvr_per)



st.write('---')

if kodeEmiten :
    
    tickerData1 = yf.Ticker(kodeEmiten)                                        
    tickerDf1 = tickerData1.history(period=data_period, interval=data_interval) 

    string_logo = '<img src=%s>' % tickerData1.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)  
    string_name = tickerData1.info['longName']                          
    st.header('**%s**' % string_name)  

    string_summary = tickerData1.info['longBusinessSummary']      
    translation = translator.translate(string_summary, dest='id')
    st.info(translation.text)

    col7, col8 = st.columns(2)
    data = yf.download(tickers=kodeEmiten, period=data_period, interval=data_interval)
    config = {'displayModeBar': False}
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                        open=data['Open'],
                                        high=data['High'],
                                        low=data['Low'],
                                        close=data['Close']
                                        )])
    fig.update_layout(title_text='Grafik ' + str(kodeEmiten), xaxis_rangeslider_visible=False, xaxis_fixedrange=True, yaxis_fixedrange=True, hovermode='x', legend_orientation='v')
    col7.plotly_chart(fig, use_container_width=True, config=config)
    
    dataEmiten = yf.Ticker(kodeEmiten)
    hargaEmiten = dataEmiten.history(period='1d')
    estEmiten = round(hargaEmiten, 3)
    kenaikanEm = (estEmiten['Close'][0] - estEmiten['Open'][0])
    kenaikanEm = round(kenaikanEm, 3)
    col8.header('Pergerakan ' + (str(kodeEmiten)) +" Hari Ini")
    col8.metric('Harga', estEmiten['Close'][0], kenaikanEm)

    tickEm = kodeEmiten
    dataEm = yf.Ticker(tickEm)
    hargaEm = dataEm.history(period='1d')
    estEm = round(hargaEm, 3)
    highEm = round(estEm['High'][0], 3)
    col8.metric('Tertinggi', highEm)
    lowEm = round(estEm['Low'][0], 3)
    col8.metric('Terendah', lowEm)

    st.write("### Valuasi")
    col9, col10, col11, col12 = st.columns(4)

    mc = web.get_quote_yahoo(kodeEmiten)['marketCap']
    mcEd = numerize.numerize(int(mc))
    col9.metric("Market Cap", mcEd)

    per = web.get_quote_yahoo(kodeEmiten)['trailingPE']
    col10.metric("PER", per)

    per = web.get_quote_yahoo(kodeEmiten)['priceToBook']
    col11.metric("PBV", per)

    st.write("### Data Saham " + str(kodeEmiten))
    data_saham = st.selectbox('‎ ', ['History', 'Pemegang Saham', 'Pendapatan'])
    if data_saham == 'History':
        st.write(tickerDf1)
    if data_saham == 'Pemegang Saham':
        tickerData1.major_holders
        tickerData1.institutional_holders
    if data_saham == 'Pendapatan':
        dataEarn = pd.DataFrame(tickerData1.earnings.T)
        st.write(dataEarn)
    

st.markdown(hide_menu, unsafe_allow_html=True)