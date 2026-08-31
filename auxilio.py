import streamlit as st

def centralizar(pri,sec,ter,texto):
    col1,col2,col3=st.columns([pri,sec,ter])
    with col2:
        st.write(texto)

def apresentacao():
    with st.expander("Quem sou eu?",width="stretch",expanded=True):

        col1,col2 = st.columns([1,2.5])
        with col1:
            st.image("imagens/eu.jpeg",width=250)
        with col2:

            with st.expander("Vida pessoal"):
                st.markdown("""Meu nome é Yuri, moro no Sul de Minas Gerais e tenho 24 anos.  
                    Gosto muito de aprender coisas novas, independente do que seja.  
                    Pratico Muay Thai e já fui competidor, mas hoje em dia pratico apenas por hobby sempre
                    que posso.  
                    Já fui militar do Exército Brasileiro, uma experiência que me proporcionou diversos
                    aprendizados""")
            st.space("small")

            with st.expander("Formação e competências"):
                st.markdown("""Em 2026 me graduei em Administração pelo **Centro Universitário Vale do Rio Verde - UNINCOR** e 
                            atualmente exerço a função de **Assistente de Importação** na 
                            <a href='https://www.linkedin.com/company/inter-aduaneira-import-export/posts/?feedView=all'>
                            Inter Aduaneira.
                            </a><br>    
                            Desde 2022 estudo o idioma **Inglês** e atualmente me encontro no nível B2 
                            (Intermediário/Avançado).<br>
                            Consigo manter um conversa com qualquer pessoa no mundo, mas
                            ainda tenho dificuldade em usar o idioma de forma profissional.""",unsafe_allow_html=True)
            st.space("small")

            with st.expander("Um pouco mais"):
                st.markdown("""Desenvolvi esse pequeno site usando a biblioteca **streamlit** do Python, personalizando com CSS.
                            O intuito desse site não é ser o melhor site com as melhores funcionalidade,
                            é divulgar meus projetos pessoais como um portifólio.""")

def carregar_css():

    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def repartir_texto_coluna(col1,col2,texto,imagem,width):
    coluna1,coluna2 = st.columns([col1,col2])
    with coluna1:
        st.markdown(texto,unsafe_allow_html=True)
    with coluna2:
        st.image(imagem,width=width)

def duas_col(col1,col2,texto,imagem,width):
    colA,colB = st.columns([col1,col2])
    with colA:
        st.image(imagem,width=width)
    with colB:
        st.markdown(texto,unsafe_allow_html=True)

@st.dialog("AVISO")
def home():
    import time
    st.info("Você será direcionado para a página inicial...")
    time.sleep(3)
    st.switch_page("pages/excel/home_excel.py")

@st.dialog(title="Download em andamento")
def baixando():
    import time
    st.success("Baixando...")
    time.sleep(3)
    st.rerun()

def mostrar_pbi():
    link="https://app.powerbi.com/view?r=eyJrIjoiOTNmNWZkM2EtNjFkMS00N2MzLWExMWUtYWY3MDBlNTE1YjJjIiwidCI6IjljOTAzNDUwLTQ3OTYtNDI1Yy05NzYxLTc4MmM5NzY4YjA5ZSJ9"
    st.iframe(link,height=600)