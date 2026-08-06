import streamlit as st
from auxilio import carregar_css

carregar_css()

st.title("Projetos de Excel",text_alignment="center")

st.space("medium")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Projeto 1**",text_alignment="center")
        st.markdown("<u>Dasboard de vendas em Excel</u>",text_alignment="center",unsafe_allow_html=True)
        st.markdown(f"""Dashboard construído 100% em Excel, desde a base de 
                    dados até as funcionalidades do Dashboard.""")
        st.image("imagens/dashboard_venda_excel.png")
        colunaA,colunaB,colunaC = st.columns([1.2,2,1])
        with colunaB:
            if st.button("Ver projeto",key="dash-vendas"):
                st.switch_page("pages/excel/dashboard_vendas.py")

with col2:
    with st.container(border=True):
        st.markdown("**Projeto 2**",text_alignment="center")
        st.markdown("<u>Relatório de Importação</u>",text_alignment="center",unsafe_allow_html=True)
        st.markdown(f"""Dashboard construído 100% em Excel, utilizando base de dados de importação
        fictícia gerada com IA.""")
        st.image("imagens/dash_import.png")
        colunaA,colunaB,colunaC = st.columns([1.2,2,1])
        with colunaB:
            if st.button("Ver projeto",key="dash-imp"):
                st.switch_page("pages/excel/dashboard_import.py")



with col3:
    with st.container(border=True):
        st.markdown("**Projeto 3**",text_alignment="center")
        st.markdown("EM BREVE")

with col4:
    with st.container(border=True):
        st.markdown("**Projeto 4**",text_alignment="center")
        st.markdown("EM BREVE")
