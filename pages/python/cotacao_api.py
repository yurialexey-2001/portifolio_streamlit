import streamlit as st
import yfinance as yf
import plotly.express as px
from auxilio import carregar_css,home
from datetime import timedelta

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

st.title("Cotação de moedas via API Yahoo Finance",text_alignment="center")

st.markdown("""Busca cotação de algumas moedas e converte em real. Esse projeto usa a API do yahoo finance, e por esse motivo 
            pode travar ou demorar um pouco. Caso isso aconteça, apague as moedas selecionadas e tente novamente.""")

col1,col2,col3 = st.columns([1.5,1,1])
with col1:
    moedas_selec = st.multiselect(label="Selecione a(s) moeda(s) que deseja visualizar",
                                  options=moedas.keys(),placeholder="Selecione uma opção")
with col2:
    data_inic = st.date_input("Data inicial",format="YYYY-MM-DD")
with col3:
    data_fim = st.date_input("Data final",format="YYYY-MM-DD") 

if moedas_selec and data_inic and data_fim:

    if len(moedas_selec) == 1 and data_fim - data_inic == timedelta(days=0):
        moeda = yf.Ticker(moedas[moedas_selec[0]])
        cotacao = moeda.history(start=data_inic,end=data_fim + timedelta(days=1))
        cotacao = cotacao["Close"]
        cotacao_final = cotacao.iloc[-1]

        st.metric(label=f"Valor de {moedas_selec[0]}",value=f"R$ {round(cotacao_final,4)}")

    elif len(moedas_selec) > 1 and data_fim - data_inic == timedelta(days=0):
        for i in moedas_selec:
            moeda = yf.Ticker(moedas[i])
            cotacao = moeda.history(start=data_inic,end=data_fim + timedelta(days=1))
            cotacao = cotacao["Close"]
            cotacao_final = cotacao.iloc[-1]

            st.metric(label=f"Valor de {i}",value=f"R$ {round(cotacao_final,4)}")

    elif len(moedas_selec) == 1 and data_fim - data_inic > timedelta(days=0):
        moeda = yf.Ticker(moedas[moedas_selec[0]])
        cotacao = moeda.history(start=data_inic,end=data_fim + timedelta(days=1))
        cotacao = cotacao["Close"].rename("Preço do dia em R$")
        cotacao.index = cotacao.index.strftime("%d/%m/%Y")
        
        col1,col2 = st.columns([1,3])
        with col1:
            st.table(cotacao,width=1500,border=True,height=350)

        with col2:
            if data_fim - data_inic > timedelta(days=10):
                cotacao = moeda.history(start=data_inic,end=data_fim)
                cotacao = cotacao["Close"]
                cotacao = cotacao.reset_index()
                grafico = px.line(cotacao,x=cotacao["Date"],y=cotacao["Close"],
                                  title=f"Variação do preço de {moedas_selec[0]} ao longo do período selecionado",

                                )
                grafico.update_layout(
                        xaxis_title="Data",
                        yaxis_title="Taxa Cambial em R$",)

                grafico.update_traces(line_color="green")
                st.plotly_chart(grafico)

colA,colB = st.columns(2)
with colB:
    if st.button("Ir para Home",width="stretch"):
        home("python")