
import streamlit as st
from auxilio import carregar_css,home

carregar_css()

st.page_link("pages/python/cotacao_api.py",label="Voltar",icon="⬅️")

st.title("Documentação do projeto",text_alignment="center")

st.header("Inspiração para criação desse projeto")
with st.container(border=True):
    st.markdown("""Todos os dias no trabalho preciso checar a taxa cambial de moedas em determinadas datas,
    porém a plataforma utilizada pela empresa requer licença paga.<br>
     Pensando nisso, criei esse projeto que utiliza
    da mesma lógica dessa plataforma, porém de forma gratuita e simples.""",unsafe_allow_html=True)

st.header("Como utilizar")
with st.container(border=True):

    st.subheader("Escolhendo a moeda")
    st.markdown("""Selecione, no primeiro campo, qual a(s) moeda(s) deseja visualizar.<br>
    É importante destacar que há somente algumas moedas disponíveis para visualização.""",unsafe_allow_html=True)

    st.image("imagens/campo_moeda.png",caption="Dólar selecionado apenas a fim de exemplo")

    st.subheader("Período de visualização")

    st.markdown("""O período de visualização precisa seguir algumas regras de acordo com o que o usuário desejar.
                O campo **Data inicial** vai receber a data de início da análise. Portanto, É 
                <span style='color: red;'>OBRIGATÓRIO</span> que 
                seja uma data mais antiga que a data do campo **Data final**, exceto quando o usuário
                buscar pela taxa cambial de um dia específico. Nesse caso, as duas datas devem ser inseridas iguais.
                Para as situações mencionadas acima, cada uma retornará um output diferente.
    """,unsafe_allow_html=True)

    st.markdown("##### • Data inicial e Data final iguais:")
    st.markdown("""No caso das duas datas inseridas iguais, a aplicação retornará a taxa cambial da(s) moeda(s) 
            selecionada(s) naquela data. Exemplo:""")
    st.image("imagens/datas_iguais_out.png")
    st.markdown("""Caso insira mais de uma moeda, vários cards como esse serão retornados, um pra cada moeda.""")

    st.markdown("##### • Data inicial e Data final diferentes:")
    st.markdown("""No caso das duas datas inseridas diferentes, a aplicação retornará a taxa cambial da(s) moeda(s) 
               selecionada(s) em todos os dias entre o intervalo das duas datas. Exemplo:""")
    st.image("imagens/datas_dif_out.png")

    st.markdown("##### • Extra:")
    st.markdown("""Caso a diferença entre a Data inicial e a Data final seja maior que 10 dias além da tabela
    com a taxa cambial durante o período, a aplicação também retornará um pequeno gráfico da variação dessa taxa
    ao longo do período selecionado. Exemplo:""")
    st.image("imagens/graficos_yahoo.png")
    st.markdown("""<span style='color: red;'>
                No momento, essa funcionalidade só está disponível quando há apenas uma moeda selecionada.</span>""",
                unsafe_allow_html=True,text_alignment="center")

st.header("Considerações finais")
with st.container(border=True):
    st.markdown("""Esse projeto é uma versão melhorada de algo que fiz no passado. Usei a mesma lógica, 
    porém otimizando as funcionalidades.
    Nesse projeto, utilizei as seguintes bibliotecas no python:<br><br>
    • **streamlit**: blocos de input para que o usuário possa inserir as informações que deseja;<br>
    • **yfinance**: biblioteca que conecta  o Python a API do Yahoo Finance e busca a cotação das moedas;<br>
    • **plotly.express**: biblioteca de gráficos que se conecta facilmente com streamlit;<br>
    • **datetime**: biblioteca para tratamento de dados de tempo (dia, hora, etc).""",
    unsafe_allow_html=True)

with st.expander("Clique aqui para ver o código para da aplicação"):
    st.code(body="""
import streamlit as st
import yfinance as yf
import plotly.express as px
from datetime import timedelta

moedas = {"Dólar Americano": "USDBRL=X",
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
                                  title=f"Variação do preço de {moedas_selec[0]} ao longo do período selecionado")
                grafico.update_layout(
                                    xaxis_title="Data",
                                    yaxis_title="Taxa Cambial em R$",)
                
                grafico.update_traces(line_color="green")
                                  
                st.plotly_chart(grafico)
        
            """
        ,language="python")

colA,colB = st.columns(2)
with colB:
    if st.button("Ir para Home",width="stretch"):
        home("python")






