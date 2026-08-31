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

st.caption("Dashboard disponível para interação",text_alignment="center")

col1,col2 = st.columns([2,4])

with col1:
    st.header("Apresentação")
with col2:
    st.space("small")
    st.badge("Em desenvolvimento",color="yellow")

with st.container(border=True):
    st.subheader("O que é o Prouni?")

    st.markdown("""O PROUNI (Programa Universidade para Todos) é um programa do governo federal, criado em 2004,
     que oferece bolsas de estudos integrais e parciais em faculdades particulares. O objetivo do programa
     é facilitar o acesso de estudantes de baixa renda ao ensino superior. <br>
     Para saber mais sobre o programa, clique <a href="https://www.gov.br/mec/pt-br/prouni"> aqui</a>.
     """,unsafe_allow_html=True)

    st.subheader("Objetivo")

    st.markdown("""O objetivo desse projeto foi analisar os últimos 5 anos (2021 a 2025) de concessão de 
    bolsas do PROUNI, onde os filtros principais são o **ANO DE CONCESSÃO** e o **ESTADO DE ORIGEM** dos bolsistas.""")

st.header("Perguntas e Indicadores respondidos pelo projeto")

with st.container(border=True):

    st.subheader("- Qual o total de bolsas concedidas?")
    st.markdown("""Aplicando os filtros é possível analisar o total de bolsas concedidas por Ano, Estado, Sexo, Curso,
      e outras categorias.""")

    st.subheader("- Qual o percentual de bolsistas portadores de deficiência física?")
    st.markdown("""Através do card, é possível visualizar a porcentagem de pessoas com deficiência física
    em relação ao total de bolsistas do filtro aplicado.<br> Além disso, ao posicionar o mouse sobre o card, é possível 
    visualizar a quantidade exata de pessoas com deficiência por sexo.""",unsafe_allow_html=True)

    st.subheader("- Idade Média dos Bolsistas")
    st.markdown("""A idade média dos bolsistas no momento da concessão da bolsa.""")

    st.subheader("- Distribuição Nacional dos Bolsistas")
    st.markdown("""Através do Mapa (que também é um dos filtros do dashboard) é possível visualizar a distribuição dos 
    bolsistas no país. Esse indicador aponta o Estado de origem do bolsista, e não onde a Universidade onde a bolsa foi 
    concedida. <br>Além disso, ao posicionar o mouse sobre os Estados, 
    é possível ver as 5 cidades com mais bolsistas do Estado.""",unsafe_allow_html=True)

    st.subheader("- Quais os cursos mais procurados pelo Bolsista PROUNI?")
    st.markdown("""O gráfico de barras empilhadas mostra pefeitamente os cursos com maior procura pelo bolsista
    PROUNI.<br>Além disso, a barra está divida também por gênero, para que seja mensurável a utilização das bolsas
     também por genêro. """,unsafe_allow_html=True)

