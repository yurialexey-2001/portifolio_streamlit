import streamlit as st
from auxilio import carregar_css,mostrar_pbi

carregar_css()

col1,col2 = st.columns([1,10])
with col1:
    st.page_link("pages/power_bi/home_pbi.py",label="Home",icon="🏠")
with col2:
    st.page_link("pages/power_bi/analise_prouni_doc.py",label="Documentação",icon="📖")

st.title("Análise de concessão de Bolsas do PROUNI de 2021 a 2025",text_alignment="center")

mostrar_pbi()