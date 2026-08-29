import streamlit as st
from auxilio import carregar_css

carregar_css()

st.page_link("pages/geral/sobre_mim.py",label="Início",icon="🧑‍🦰")

st.title("Projetos de Python",text_alignment="center")

st.space("medium")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Projeto 1**",text_alignment="center")

        st.markdown("**Cotação de moedas**",text_alignment="center")
        
        st.markdown("""Cotação de moedas usando a biblioteca yfinance, que faz conexão com a API
                    do Yahoo Finance.""")
        st.image("imagens/graficos_yahoo.png")
        if st.button("Ver projeto",key="cotacao-python",use_container_width=True):
            st.switch_page("pages/python/cotacao_api.py")

