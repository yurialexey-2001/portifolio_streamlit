import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from auxilio import carregar_css

carregar_css()

col1,col2 = st.columns([1,10])
with col1:
    st.page_link("pages/python/home_python.py",label="Home",icon="🏠")
with col2:
    st.page_link("pages/python/cotacao_api_doc.py",label="Documentação",icon="📖")

moedas = {  "Dólar Americano": "USDBRL=X",
            "Euro": "EURBRL=X",
            "Libra Esterlina": "GBPBRL=X",
            "Iene Japonês": "JPYBRL=X",
            "Franco Suíço": "CHFBRL=X",
            "Dólar Canadense": "CADBRL=X",
            "Dólar Australiano": "AUDBRL=X",
            "Yuan Chinês": "CNYBRL=X",
            "Peso Argentino": "ARSBRL=X",
            "Peso Mexicano": "MXNBRL=X",
            "Peso Chileno": "CLPBRL=X",
            "Rand Sul-Africano": "ZARBRL=X"}

periodos = {
    "1 dia": "1d",
    "5 dias": "5d",
    "1 mês": "1mo",
    "3 meses": "3mo",
    "6 meses": "6mo",
    "1 ano": "1y",
    "2 anos": "2y",
    "5 anos": "5y",
    "10 anos": "10y",
    "Ano atual": "ytd",
    "Máximo": "max"
}

st.title("Cotação de moedas via API Yahoo Finance",text_alignment="center")

st.markdown("""Busca cotação de algumas moedas e converte em real. Esse projeto usa a API do yahoo finance, e por esse motivo 
            pode travar ou demorar um pouco. Caso isso aconteça, apague as moedas selecionadas e tente novamente.""")

col1,col2 = st.columns([3,1])
with col1:
    moedas_selec = st.multiselect(label="Selecione a(s) moeda(s) que deseja visualizar",options=moedas.keys())
with col2:
    periodo_selec = st.multiselect(label="Selecione o período",options=periodos.keys(),
                                   default="1 dia",
                                   max_selections=1,width=200)

if moedas_selec and periodo_selec:
    if len(moedas_selec) == 1 and periodos[periodo_selec[0]] == "1d":

        cotacao = yf.download(moedas[moedas_selec[0]],period=periodos[periodo_selec[0]])
        cotacao.columns = cotacao.columns.droplevel(1)
        cotacao = cotacao["Close"]
        
        st.metric(label=f"Valor de {moedas_selec[0]}",value=f"R$ {round(cotacao.iloc[-1],2)}",width="content")

    elif len(moedas_selec) > 1 and periodos[periodo_selec[0]] == "1d":
        for i in moedas_selec:
            cotacao = yf.download(moedas[i],period=periodos[periodo_selec[0]])
            cotacao.columns = cotacao.columns.droplevel(1)
            cotacao = cotacao["Close"] 
            st.metric(label=f"Valor de {i}",value=f"R$ {round(cotacao.iloc[-1],2)}",width="content")

    elif periodos[periodo_selec[0]] != "1d":
        df = pd.DataFrame()
        for i in moedas_selec:
            cotacao = yf.download(moedas[i],period=periodos[periodo_selec[0]])
            cotacao.columns = cotacao.columns.droplevel(1)

            df[i] = cotacao["Close"]
            
        fig = px.line(df,x=df.index,y=df.columns)

        st.plotly_chart(fig, use_container_width=True)
        