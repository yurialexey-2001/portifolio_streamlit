import streamlit as st
import time
from auxilio import carregar_css,repartir_texto_coluna,home,baixando


carregar_css()

st.page_link("pages/excel/home_excel.py",label="Home",icon="🏠")

st.title("Dashboard de Despesas de Importação",text_alignment="center")

st.header("Case")
with st.container(border=True):
    col1,col2 = st.columns([1,5])
    with col1:
        st.image("imagens/logistica inter.png",width=250)
    with col2:
        st.markdown("""A empresa ***Logística Internacional*** é uma empresa que atua no setor de 
        Comércio Exterior há 2 anos. Localizada em Campanha-MG, atende clientes de todo o Brasil
        que desejam importar produtos dentro de algumas categorias específicas.
        A empresa buscava consolidar informações e obter insights relevantes através de suas planilhas de Excel longas e cheias
        de dados. Para simular esse cenário, foi gerada uma base de dados com aproximadamente 20 mil registros de de embarques
        de importação e as despesas desses embarques.
        """)

st.header("Apresentação")
with st.container(border=True):
    st.subheader("Objetivo")
    texto = """Apontar indicadores relevantes para a empresa, bem como acompanhar as despesas de cada embarque
    e monitorar o andamento da operação através do dashboard criado a partir de uma planilha no Excel."""
    repartir_texto_coluna(col1=1.3,col2=2,texto=texto,imagem="imagens/dash_import.png",width=600)


    st.subheader("Desafio proposto")
    st.markdown("""Empresas que realizam importações normalmente possuem centenas ou milhares de DI's ao longo do ano, 
    tornando difícil responder perguntas como:

- **Qual categoria possui maior custo?**<br>
- **Quais despesas representam a maior parcela do processo?**<br>
- **Como está a distribuição dos canais de parametrização?**
""",
unsafe_allow_html=True)

    st.subheader("O que foi desenvolvido")
    st.markdown(r"""
                - Dashboard 100% em Excel
                - Base de dados com mais de 20 mil registros
                - Dados modelados e projetados para que o importador tenha uma visão do andamento
                da operação.""")
    st.subheader("Filtros utilizados")
    st.markdown("""
                    - Ano
                    - Categoria
                    - Subcategoria""")
    st.subheader("KPI's selecionados")

    col1,col2,col3 = st.columns([1,10,1])
    with col2:
        with st.expander("Porcentagem de embarques por modal"):
            texto = r"""Utilizando um **gráfico de pizza**, fica visívelmente nítida a diferença entre a quantidade de 
            embarques por modal, onde aproximadamente 70% dos embarques são pelo modal **Marítmo.**<br><br>
            """
            repartir_texto_coluna(col1=1,col2=1.5,texto=texto,imagem="imagens/pizza import.png",width=500)

            st.markdown("""***Dados obtidos:***<br><br>
                        - ***702*** embarques marítmos, sendo ***474*** em 2025 e ***228*** em 2026;<br>
                        - ***298*** embarque aéreos, sendo ***199*** em 2025 e ***99*** em 2026;""",unsafe_allow_html=True)

        with st.expander("Distribuição das despesas"):
            st.markdown("""Para representar a distribuição das despesas, o gráfico ideal é o 
            **gráfico de barras empilhadas**. Com ele, é possível visualizar as despesas em formato de ranking. 
            Dessa forma, além do valor da despesa é possível saber quais foram as maiores despesas. 
            Junto a ele, uma **tabela com a porcentagem** que a despesa representa sobre as despesas gerais auxilia
            muito no entendimento do quão importante é a despesa.""",unsafe_allow_html=True)

            ima1,ima2=st.columns([2,1.5])
            with ima1:
                st.image("imagens/despesas imp.png")
            with ima2:
                st.image("imagens/% imp.png",width=300)
            st.markdown("***Dados obtidos com a visualização desse gráfico:***")

            st.markdown(r"""
                    - Impostos são, majoritariamente, a maior despesa de todas as categorias;<br>
                    - O ICMS representa cerca de **30%** das despesas gerais de todas as categorias;<br>
                    - A categoria de eletrônicos tem a maior relação demurrage/despesas totais, com um percentual de 
                    **1,08%** em relação as despesas totais. Isso pode se dar ao fato da carga ser "frágil", e exigir
                    um certo cuidado para a retirada da mesma.
                    """,
                    unsafe_allow_html=True)

        with st.expander("Parametrização dos processos"):

            texto ="""Cards são o ideal para representar o número de processos em cada canal de parametrização da
            Receita Federal. Dessa forma, é possível analisar como está o andamento e a liberação dos processos
            pela Receita.<br><br>
            ***Informação relevante após análise dos cards***:<br><br>
            - A categoria **Químicos** em 2025 teve 10 processos parametrizados em Canal Vermelho pela Receita Federal. 
            Porém, até junho de 2026, já possuía 11 processos parametrizados nesse Canal. Será necessário uma ação
            maior e um cuidado maior no registro de DUIMPS para essa categoria, visando evitar dores de cabeça e 
            procedimentos burocráticos.
            """

            repartir_texto_coluna(col1=2,col2=1,texto=texto,imagem="imagens/parametrizacao.png",width=200)

        with st.expander("Custo médio por embarque"):

            st.image("imagens/custo médio embarque.png",use_container_width=True)

            st.markdown("""Assim como o próprio nome do indicador diz, esse card visa mensurar o 
             **Custo médio por embarque**. Com esse indicador, o importador consegue ter uma visão de
              qual é o custo médio de cada embarque naquela categoria. Com isso, a mensuração e planejamento
               financeiro é possível, o que agiliza o processo e permite que a operação aconteça de maneira
                rápida e eficiente. """)

st.header("Conclusão")
with st.container(border=True):
    st.markdown("""Com esse projeto, foi possível extrair alguns dados da planilha que a empresa 
    ***Logística Internacional*** possui, construir um dashboard para a empresa e analisar alguns pontos cruciais e 
    muito importantes para operações na área da importação.""")

st.header("Veja a interação do Dashboard",text_alignment="center")
st.video("videos/dash_imp_interacao.mp4")

col1,col2 = st.columns([1,1])
with col1:
    with open("bases de dados/RELATORIO FICTICIO DESPESAS DE IMPORTAÇÃO.xlsx", "rb") as dash_imp:
        if st.download_button(
            "Baixar base de dados + dashboard",
            width="stretch",
            data=dash_imp,
            file_name="Base + Dashboard.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            baixando()
with col2:
    if st.button("Ir para Home",width="stretch"):
        home("excel")
