import streamlit as st
from auxilio import carregar_css

carregar_css()

st.title("Projetos de Python",text_alignment="center")

st.space("medium")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Projeto 1**",text_alignment="center")

        st.markdown("Cotação de moedas",text_alignment="center")
        
        st.markdown("""Cotação de moedas usando a biblioteca yfinance, que faz conexão com a API
                    do Yahoo Finance.""")
        st.image("imagens/graficos_yahoo.png")
        colunaA,colunaB,colunaC = st.columns([1.2,2,1])
        with colunaB:
            if st.button("Ver projeto"):
                st.switch_page("pages/python/cotacao_api.py")


with col2:
    with st.container(border=True):
        st.markdown("**Projeto 2**",text_alignment="center")
        st.markdown("EM BREVE")



with col3:
    with st.container(border=True):
        st.markdown("**Projeto 3**",text_alignment="center")
        st.markdown("EM BREVE")

with col4:
    with st.container(border=True):
        st.markdown("**Projeto 4**",text_alignment="center")
        st.markdown("EM BREVE")