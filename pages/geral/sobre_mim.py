import streamlit as st
from auxilio import duas_col,apresentacao, carregar_css

carregar_css()

st.title("Olá, seja bem vindo!",text_alignment="center")

st.space("small")

apresentacao()

st.space("small")
st.subheader("Tecnologias que utilizo",text_alignment="center")

col1,col2 = st.columns([1,1])

#expander do Python e SQL
with col1:
    with st.expander("Python",width="stretch",expanded=True):
        texto = """**Nível intermediário**<br>
                Posso criar programas lógicos bem como desenvolver automações e utilizar a ferramenta para
                tratamento e análise de dados. Esse site, por exemplo, foi 100% criado
                dentro do Python. Atualmente me encontro estudando a linguagem e adquirindo mais
                conhecimento para aprimorar ainda mais meus projetos."""
        duas_col(1,5,texto=texto,imagem="imagens/logo do python.png",width=50)

        if st.button("Clique aqui para ver meus projetos de Python",use_container_width=True):
            st.switch_page("pages/python/home_python.py")
    st.space("small")
        
    with st.expander("SQL",width="stretch",expanded=True):
        texto="""**Nível Intermediário**<br>
                    Posso realizar consultas e cruzar informações para extrair insights relevantes 
                    de bancos de dados relacionais. Utilizo o SQL integrado com outras ferramentas para
                    visualização de dados, como **Python** e **Power BI**. Projetos sendo trabalhados para 
                     posterior publicação"""
        duas_col(1,5,texto=texto,imagem="imagens/logo do sql.png",width=50)
        if st.button("Clique aqui para ver meus projetos em SQL",use_container_width=True):
            st.switch_page("pages/sql/home_sql.py")


#expander do Excel e Power BI

with col2:
    with st.expander("Excel",width="stretch",expanded=True):
        texto="""**Nível intermediário**<br> 
                Posso construir Dashboards interativos,
                conheço uma vasta quantidade de fórmulas para diversos fins e também utilizo o Power Query
                dentro do Excel para tratamento de dados, além. utilizo Excel no trabalho
                diariamente e hoje me encontro estudando ainda mais
                a ferramenta para atingir o **nível avançado**.
                """
        duas_col(1,5,texto=texto,imagem="imagens/logo do excel.png",width=50)
        if st.button("Clique aqui para ver meus projetos em Excel",use_container_width=True):
            st.switch_page("pages/excel/home_excel.py")  
    st.space("small")

    with st.expander("Power BI",width="stretch",expanded=True):
        texto="""**Nível básico**<br>
                Posso utilizar o Power Query dentro do Power BI para o tratamento de dados com
                confiança, criar relacionementos
                entre as tabelas do banco de dados, criar medidas simples utilizando fórmulas DAX e criar
                dashboards que comunicam insights sem poluí-lo com design mirabolante."""
        duas_col(1,5,texto=texto,imagem="imagens/logo do pbi.png",width=150)
        if st.button("Clique aqui para ver meus projetos em Power BI",use_container_width=True):
            st.switch_page("pages/pbi/home_pbi.py")


st.space("medium")

st.subheader("Conecte-se comigo nas redes!",text_alignment="center")


#redes sociais
coluna1,coluna2,coluna3,coluna4 = st.columns([5,0.5,0.5,5])

with coluna2:
    st.image("imagens/logo_github.webp",link="https://github.com/yurialexey-2001",width=60,)
with coluna3:
    st.image("imagens/logo linkedin.png",link="https://www.linkedin.com/in/yuri-oliveira-6a1bb1240/",width=60)

