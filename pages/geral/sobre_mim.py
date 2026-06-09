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
    with st.expander("Python",width="stretch"):
        texto = """**Nível intermediário**<br>
                Posso criar programas lógicos bem como desenvolver automações e utilizar a ferramenta para
                tratamento e análise de dados. Me encontro estudando a linguagem e adquirindo mais
                conhecimento para aprimorar ainda mais meus projetos."""
        duas_col(1,5,texto=texto,imagem="imagens/logo do python.png",width=50)

        if st.button("Clique aqui para ver meus projetos de Python"):
            st.switch_page("pages/python/home_python.py")
    st.space("small")
        
    with st.expander("SQL",width="stretch"):
        texto="""**Nível Intermediário**<br>
                    Posso realizar consultas e cruzar informações para extrair insights relevantes 
                    de bancos de dados relacionais. Utilizo o SQL integrado com outras ferramentas para
                    visualização de dados, como **Python** e **Power BI**."""
        duas_col(1,5,texto=texto,imagem="imagens/logo do sql.png",width=50)
        if st.button("Clique aqui para ver meus projetos em SQL"):
            st.switch_page("pages/sql/sql.py")



#expander do Excel

with col2:
    with st.expander("Excel",width="stretch"):
        texto="""**Nível intermediário**<br> 
                Posso construir Dashboards interativos,
                conheço uma vasta quantidade de fórmulas para diversos fins e também utilizo 
                para tratamento e análise de dados. Me encontro estudando ainda mais
                a ferramenta para atingir o **nível avançado**.
                """
        duas_col(1,5,texto=texto,imagem="imagens/logo do excel.png",width=50)
        if st.button("Clique aqui para ver meus projetos em Excel"):
            st.switch_page("pages/excel/home_excel.py")  

st.space("medium")

st.subheader("Conecte-se comigo nas redes!",text_alignment="center")


#redes sociais
coluna1,coluna2,coluna3,coluna4 = st.columns([5,0.5,0.5,5])

with coluna2:
    st.image("imagens/logo_github.webp",link="https://github.com/yurialexey-2001",width=60,)
with coluna3:
    st.image("imagens/logo linkedin.png",link="https://www.linkedin.com/in/yuri-oliveira-6a1bb1240/",width=60)