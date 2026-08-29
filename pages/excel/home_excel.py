import streamlit as st
from auxilio import carregar_css

carregar_css()

st.page_link("pages/geral/sobre_mim.py",label="Início",icon="🧑‍🦰")

st.title("Projetos de Excel",text_alignment="center")

st.space("medium")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Projeto 1**",text_alignment="center")
        st.markdown("**Dasboard de vendas em Excel**",text_alignment="center")
        st.markdown(f"""Dashboard construído 100% em Excel, desde a base de 
                    dados até as funcionalidades do Dashboard.""")
        st.image("imagens/dashboard_venda_excel.png")
        if st.button("Ver projeto",key="dash-vendas",use_container_width=True):
                        st.switch_page("pages/excel/dashboard_vendas.py")

with col2:
    with st.container(border=True):
        st.markdown("**Projeto 2**",text_alignment="center")
        st.markdown("**Relatório de Importação**",text_alignment="center")
        st.markdown(f"""Dashboard construído 100% em Excel, utilizando base de dados de importação
        fictícia gerada com IA.""")
        st.image("imagens/dash_import.png")
        if st.button("Ver projeto",key="dash-imp",use_container_width=True):
            st.switch_page("pages/excel/dashboard_import.py")




