
import streamlit as st

st.page_link("pages/python/cotacao_api.py",label="Voltar",icon="⬅️")

st.title("Construção do projeto",text_alignment="center")

st.header("Métodos utilizados")
with st.container(border=True):

    st.subheader("Bibliotecas utilizadas")

    st.markdown("""
                As bibliotecas utilizadas para esse projeto foram:
                
                - **streamlit**: criação visual no site;
                - **yfinance**: biblioteca para puxar os dados da API do Yahoo Finance;
                - **pandas**: criação do dataframe para posterior criação de gráfico;
                - **plotly**: gráfico.""")
    
    st.code(language="python",body="""import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd""")



    st.markdown("""Os códigos das moedas e períodos que podem ser utilizados no Yahoo Finance seguem um padrão. 
                Como esse padrão pode ser confuso para o usuário, criei esses dicionários para que 
                o usuário selecione uma opção e o Yahoo Finance entenda essa opção dentro de
                suas possibilidades. Abaixo os dicionários **moedas** e **periodos.**""")
    st.code(
        language="python",
        body="""moedas = { "Dólar Americano": "USDBRL=X",
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
            """)
    
    st.markdown("""Dessa forma, as opções visíveis para seleção serão as chaves do dicionário, porém o 
                Yahoo entenderá os valores.""")
    
st.header("Código para utilização da API")
with st.container(border=True):

    st.subheader("Visualização de uma moeda")
    st.markdown("""Em caso de visualização de apenas uma moeda no dia da pesquisa, o código é simples.""")

    st.code(language="python",body="""if moedas_selec and periodo_selec:
    if len(moedas_selec) == 1 and periodos[periodo_selec[0]] == "1d":

        cotacao = yf.download(moedas[moedas_selec[0]],period=periodos[periodo_selec[0]])
        cotacao.columns = cotacao.columns.droplevel(1)
        cotacao = cotacao["Close"]""")
    
    ##
    
    st.subheader("Visualização de duas ou mais moedas")
    st.markdown("""Caso o usuário selecione mais de uma moeda naquele dia, o código muda um
                pouco. É necessário um loop **for**.""")
    
    st.code(language="python",
            body="""if moedas_selec and periodo_selec:
            if len(moedas_selec) > 1 and periodos[periodo_selec[0]] == "1d":
                for i in moedas_selec:
                    cotacao = yf.download(moedas[i],period=periodos[periodo_selec[0]])
                    cotacao.columns = cotacao.columns.droplevel(1)
                    cotacao = cotacao["Close"]""")
    
    st.markdown("""Esses são os códigos da visualização de apenas um dia.""")

    ##

    st.subheader("Geração de gráfico")
    st.markdown("""A visualização do preço da(s) moeda(s) em qualquer período acima de 1 dia será
                exibida em formato de gráfico, seja uma moeda ou várias selecionadas.
                 Para isso, foi utilizado o código abaixo.""")
    
    st.code(language="python",
        body="""if moedas_selec and periodo_selec:
            if periodos[periodo_selec[0]] != "1d":
                df = pd.DataFrame()
                for i in moedas_selec:
                    cotacao = yf.download(moedas[i],period=periodos[periodo_selec[0]])
                    cotacao.columns = cotacao.columns.droplevel(1)

                    df[i] = cotacao["Close"]
        
                fig = px.line(df,x=df.index,y=df.columns)

                st.plotly_chart(fig, use_container_width=True)""")
    
    st.markdown("""Com isso, um gráfico semelhante a esse será retornado:""")
    st.image("imagens/graficos_yahoo.png")




