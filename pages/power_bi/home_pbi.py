import streamlit as st
from auxilio import carregar_css

carregar_css()

st.page_link("pages/geral/sobre_mim.py",label="Início",icon="🧑‍🦰")

st.title("Projetos de Power BI",text_alignment="center")

st.space("medium")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Projeto 1**",text_alignment="center")

        st.markdown("""**Análise da concessão de bolsas do PROUNI**""",text_alignment="center")
        
        st.markdown("""Dashboard desenvolvido a fim de analisar a concessão de bolsas do PROUNI de 2021 a 2025.""")
        st.image("imagens/analise prouni.png")

        if st.button("Ver projeto",key="dash-prouni",use_container_width=True):
            st.switch_page("pages/power_bi/analise_prouni.py")

