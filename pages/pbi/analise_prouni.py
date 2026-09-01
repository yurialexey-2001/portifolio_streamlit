import streamlit as st
from auxilio import carregar_css,mostrar_pbi,home

carregar_css()

col1,col2 = st.columns([1,10])
with col1:
    st.page_link("pages/pbi/home_pbi.py",label="Home",icon="🏠")
with col2:
    st.page_link("pages/pbi/analise_prouni_doc.py",label="Documentação",icon="📖")

st.title("Análise de concessão de Bolsas do PROUNI de 2021 a 2025",text_alignment="center")

mostrar_pbi()

st.caption("Dashboard disponível para interação",text_alignment="center")

col1,col2 = st.columns([2,4])

st.header("Apresentação")

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

st.header("Indicadores apontados pelo projeto")

with st.container(border=True):

    st.subheader("- Total de bolsas concedidas")
    st.markdown("""Aplicando os filtros é possível analisar o total de bolsas concedidas por Ano, Estado, Sexo, Curso,
      e outras categorias.<br>
      Além disso, também é possível visualizar a porcentagem do crescimento ou diminuição 
      da concessão de bolsas em relação ao ano anterior da análise.""",unsafe_allow_html=True)
    

    st.subheader("- Percentual de bolsistas portadores de deficiência física")
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

    st.subheader("- Principais cursos de concessão de bolsas")
    st.markdown("""O gráfico de barras empilhadas mostra pefeitamente os cursos com maior procura pelo bolsista
    PROUNI.<br>Além disso, a barra está divida também por gênero, para que seja mensurável a utilização das bolsas
     também por genêro. """,unsafe_allow_html=True)

    st.subheader("- Raça/Cor dos bolsistas")
    st.markdown("""Esse gráfico mostra a quantidade de bolsistas PROUNI por Raça/Cor.""")

    st.subheader("- Quantidade de bolsistas por sexo")
    st.markdown("""Diferente dos outros indicadores que indicam a quantidade de bolsistsa por sexo de acordo com uma
    categoria específica, esse gráfico mostra a quantidade total de bolsistas por sexo como um todo.<br>
    Além disso, ao posicionar o mouse sobre as barras, é possível visualizar a porcentagem que a quantidade
    em questão representa em relação ao total geral ou ao total com filtros aplicados.""",unsafe_allow_html=True)

    st.subheader("- Bolsistas por tipo de bolsa")
    st.markdown("""Mostra a quantidade de bolsistas com bolsa integral e parcial, bem como a porcentagem que 
    cada valor representa sobre a quantidade total de bolsistas ou ao total com filtros aplicados.""")

    st.subheader("- Bolsistas por modalidade")
    st.markdown("""Mostra a quantidade de bolsistas que estudam Presencial e EAD, bem como a porcentagem que 
    cada valor representa sobre a quantidade total de bolsistas ou ao total com filtros aplicados""")

st.header("Conclusão")

with st.container(border=True):
    st.markdown("""Com esse projeto pude trabalhar meus conhecimentos no **Power BI** e aplicá-los para
    que a navegação pelo Dashboard seja o mais intuitiva possível. Com os indicadores escolhidos para visualização, 
    o Dashboard responde todas as questões mencionadas acima de acordo com o(s) filtro(s) selecionado(s) pelo usuário.<br>
    Para mim, foi muito interessante o desenvolvimento desse projeto, pois pensei em desenvolver algo que não só 
    responderia meus questionamentos sobre o PROUNI, mas que também responderia os questionamentos de qualquer usuário 
    que utilizar esse projeto para quaisquer fim."""
                ,unsafe_allow_html=True)

colA,colB = st.columns(2)
with colB:
    if st.button("Ir para Home",width="stretch"):
        home("pbi")