import streamlit as st
from auxilio import carregar_css,repartir_texto_coluna,home,baixando

st.page_link("pages/excel/home_excel.py",label="Home",icon="🏠")

carregar_css()

st.title("Dashboard de Vendas",text_alignment="center")

st.header("Objetivo")
with st.container(border=True):
    col1,col2=st.columns([3,5])
    with col1:
        st.markdown("""Demonstração de habilidades na manipulação de dados no Microsoft Excel, 
                    incluindo organização, limpeza, transformação e estruturação de bases de dados para análise.<br><br>
                    Experiência na utilização de **funções**, **fórmulas avançadas** e recursos como **filtros**, **segmentações** 
                    e **gráficos** para explorar e interpretar informações de forma eficiente.<br><br>
                    Além disso, capacidade na criação de dashboards interativos e visualmente organizados, 
                    voltados para análise de indicadores e apoio à tomada de decisão, com foco em clareza, 
                    estética e usabilidade das informações apresentadas.""",unsafe_allow_html=True)
    with col2:
        st.markdown("""<br>""",unsafe_allow_html=True)
        st.image("imagens/dashboard_venda_excel.png",caption="Dashboard Pronto")

st.header("Competências aplicadas")

with st.container(border=True):
    st.markdown("""
                - Storytelling com dados  
                - Design de Dashboards  
                - Criação de KPI's""")

st.header("Metodologias utilizadas")

#explicação obtenção base de dados
with st.container(border=True):

    st.subheader("Ferramentas utilizadas")
    st.markdown("Microsoft Excel")
    
    st.subheader("Base de dados")
    texto="""A base de dados para esse projeto foi gerada dentro no Excel utilizando fórmulas e funções    
            como **ALEATÓRIO**, **PROCV**, **SOMASE** e outras.    
            Nesse projeto, optei por não usar tabelas dinâmicas para que fosse possível uma 
            personalização condicional dentro do dashboard, e para isso utilizei fórmulas e funções como
            **FILTRO**, **ÚNICO**, **ÍNDICE**, **CORRESP**, **PROCV**, **PROCX**, **SE** e outras."""
    st.markdown(texto)

    st.subheader("KPI's selecionados para visualização""")
    texto="""
            Após a geração da base de dados foi necessário selecionar alguns indicadores de desempenho
            para visualização. Os KPI's selecionados foram:   
            - **Faturamento anual por produto**  
            - **Porcentagem de vendas realizada por cada vendedor**  
            - **Total de faturamento por mês**  
            - **Funcionário que mais vendeu por mês**

            O filtro utilizado para visualização dos dados foi o **ano de vendas**.
            """
    st.markdown(texto)

st.header("Resultados antes do Dashboard")

with st.container(border=True):
    st.markdown("""
            Após a seleção dos filtros, dos indicadores de desempenho e da estruturação das
            informações, na seleção do ano o Excel nos entregava as tabelas na inseridas na imagem:""")
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.image("imagens/tabelas tratadas.png",width=850)

    st.write("""Com as fórmulas e funções aplicadas corretamente, essas tabelas funcionam como as tabelas dinâmicas,
              atualizando sempre que o ano selecionado for trocado.""")

st.header("Construção do Dashboard")

#explicação do uso de cada gráfico

with st.container(border=True):

    st.markdown("""
            Todos os gráficos utilizados foram selecionados visando:  
            - **Clareza nas informações**  
            - **Objetividade e simplicidade na visualização**  
            - **Design bonito e visualmente agradável**""")
    col1,col2,col3 = st.columns([2.5,10,1])
    with col2:

        with st.expander("Total de faturamento por mês",width=800):
        #st.subheader("Total de faturamento por mês")
            st.markdown("""O **gráfico de linhas** foi selecionado para este indicador por permitir uma visualização clara e 
                        comparativa da evolução do faturamento ao longo dos meses, 
                        facilitando a identificação de tendências e variações no período analisado.""")

            st.image("imagens/faturamento mensal.png",)

        with st.expander("Porcentagem de vendas por vendedor",width=800):
            texto="""O **gráfico de pizza** foi selecionado para este indicador por proporcionar uma visualização clara e
                            intuitiva da distribuição das vendas entre os vendedores, evidenciando a participação de cada 
                            um no volume total vendido."""
            repartir_texto_coluna(col1=1.5,col2=2,texto=texto,
                                imagem="imagens/vendas_por_vendedor.png",width=800)

        with st.expander("Faturamento Total por produto",width=800):
            texto="""O **gráfico de barras** com formatação condicional foi selecionado para este indicador por
                            permitir visualizar o comportamento do faturamento total por produto de forma clara e
                            comparativa, enquanto a formatação condicional destaca variações de desempenho, facilitando a 
                            identificação de produtos com maior ou menor faturamento."""
        
            repartir_texto_coluna(col1=1.5,col2=2,texto=texto,
                                imagem="imagens/fat por produto.png",width=500)

        with st.expander("Cards de visualização",width=800):
            texto="""
                    Os cards selecionados para visualização foram:<br><br>
                    • **Faturamento Geral Total**: permite visualizar o total faturado dentro do período analisado.<br>
                    • **Quantidade de Vendas Realizadas**: exibe o número total de vendas realizadas no período.<br>
                    • **Ticket Médio Anual**: apresenta o valor médio por venda no período analisado.<br><br>
                    Esses cards possibilitam um entendimento geral e mensurável do desempenho das vendas.
                    """
            repartir_texto_coluna(col1=1.8,col2=1,texto=texto,
                                imagem="imagens/cards.png",width=250)
            
        with st.expander("Tabela de Destaque por mês",width=800):
            st.markdown("""No centro do dashboard, foi inserida uma tabela que destaca o funcionário responsável 
                        pelo maior faturamento individual do mês, juntamente com o valor total vendido por ele.""")
            col1,col2,col3 = st.columns([1,2,1])
            with col2:
                st.image("imagens/destaques mes.png")

st.header("Conclusão")

with st.container(border=True):
    st.markdown("""
                Com este projeto, pude aprofundar meus conhecimentos na lógica por trás 
                das fórmulas do Excel e em como aplicá-las de forma estratégica para resolver diferentes problemas.<br>
                Além disso, desenvolvi a capacidade de construir um dashboard visualmente agradável e de 
                selecionar indicadores de desempenho adequados, contribuindo para análises mais precisas e assertivas.<br><br>
                É importante destacar que o principal objetivo do projeto não foi a extração de insights, 
                mas sim o treino e o desenvolvimento das habilidades no Microsoft Excel.
            """,unsafe_allow_html=True)

st.header("Veja a interação do Dashboard",text_alignment="center")
st.video("videos/dashboard_interação.mp4")


col1,col2 = st.columns([1,1])
with col1:
    with open("bases de dados/base de dados + dashboard.xlsx", "rb") as base_dash:
        if st.download_button(
            "Baixar base de dados + dashboard",
            width="stretch",
            data=base_dash,
            file_name="Base + Dashboard.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            baixando()

with col2:
    if st.button("Ir para Home",width="stretch"):
        home("excel")