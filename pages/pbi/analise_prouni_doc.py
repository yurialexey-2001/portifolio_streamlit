import streamlit as st
from auxilio import carregar_css

carregar_css()

st.page_link("pages/pbi/analise_prouni.py",label="Voltar",icon="⬅️")

st.title("Documentação do projeto",text_alignment="center")

st.header("Métodos utilizados")
with st.container(border=True):

    st.subheader("Obtenção dos dados utilizados")
    st.markdown("""Os dados utilizados para a criação desse projeto foram obtidos no site de 
    <a href='https://dadosabertos.mec.gov.br/prouni'> Dados Abertos</a> do Governo Federal. O formato de download
    selecionado foi o 'csv'.""",unsafe_allow_html=True)

    st.subheader("Importação e Tratamento dos dados")
    st.write("""Após a importação das planilhas e o acréscimo de consultas a fim de juntar as tabelas de 2020 a 2025 em apenas
    um modelo de dados, foi realizado o tratamento de dados com **Power Query**.""")

    st.markdown("Foram realizadas algumas etapas de tratamento de dados, como por exemplo na coluna de gênero:")
    col1,col2,col3,col4 = st.columns(4)

    col2.image("imagens/sexo antes.png",caption="Antes",)
    col3.image("imagens/sexo depois.png",caption="Depois")

    st.markdown("Na coluna de deficiente físico:")
    col1,col2,col3,col4 = st.columns(4)

    col2.image("imagens/deficiente antes.png",caption="Antes",)
    col3.image("imagens/deficiente depois.png",caption="Depois")

    st.markdown("""E na coluna do do tipo da bolsa:""")
    col1,col2,col3,col4 = st.columns(4)

    col2.image("imagens/tipo bolsa antes.png",caption="Antes",)
    col3.image("imagens/tipo bolsa depois.png",caption="Depois")

    st.markdown("""Para a utilização do Mapa de Formas, foi necessária a criação de uma uma Coluna Personalizada.
    Na base de dados, há somente o nome do Município do Beneficiário e a sigla do Estado. Porém, o Mapa de Formas
    não reconhece a sigla, então criei uma fórmula que pega a sigla do Estado e transforma no nome do Estado.
    Posteriormente, notei que alguns Estados ainda não eram reconhecidos pelo Mapa, devido ao acento. Então refiz
    a fórmula retirando todos eles.""",unsafe_allow_html=True)

    st.code(
        f"""= Table.AddColumn('#' "Valor Substituído3", "Personalizar", each if [UF_BENEFICIARIO] = "AC" then "Acre"
            else if [UF_BENEFICIARIO] = "AL" then "Alagoas"
            else if [UF_BENEFICIARIO] = "AP" then "Amapa"
            else if [UF_BENEFICIARIO] = "AM" then "Amazonas"
            else if [UF_BENEFICIARIO] = "BA" then "Bahia"
            else if [UF_BENEFICIARIO] = "CE" then "Ceara"
            else if [UF_BENEFICIARIO] = "DF" then "Distrito Federal"
            else if [UF_BENEFICIARIO] = "ES" then "Espirito Santo"
            else if [UF_BENEFICIARIO] = "GO" then "Goias"
            else if [UF_BENEFICIARIO] = "MA" then "Maranhao"
            else if [UF_BENEFICIARIO] = "MT" then "Mato Grosso"
            else if [UF_BENEFICIARIO] = "MS" then "Mato Grosso do Sul"
            else if [UF_BENEFICIARIO] = "MG" then "Minas Gerais"
            else if [UF_BENEFICIARIO] = "PA" then "Para"
            else if [UF_BENEFICIARIO] = "PB" then "Paraiba"
            else if [UF_BENEFICIARIO] = "PR" then "Parana"
            else if [UF_BENEFICIARIO] = "PE" then "Pernambuco"
            else if [UF_BENEFICIARIO] = "PI" then "Piaui"
            else if [UF_BENEFICIARIO] = "RJ" then "Rio de Janeiro"
            else if [UF_BENEFICIARIO] = "RN" then "Rio Grande do Norte"
            else if [UF_BENEFICIARIO] = "RS" then "Rio Grande do Sul"
            else if [UF_BENEFICIARIO] = "RO" then "Rondonia"
            else if [UF_BENEFICIARIO] = "RR" then "Roraima"
            else if [UF_BENEFICIARIO] = "SC" then "Santa Catarina"
            else if [UF_BENEFICIARIO] = "SP" then "Sao Paulo"
            else if [UF_BENEFICIARIO] = "SE" then "Sergipe"
            else if [UF_BENEFICIARIO] = "TO" then "Tocantins"
            else null)"""
                )
    st.space("small")

    st.markdown("""Além disso, criei uma Personalizada de idade, que pega o ano de concessão da Bolsa e subtrai o ano
    de nascimento do beneficiário, retornando sua idade.""")

st.header("Medidas criadas com DAX")
with st.container(border=True):

    st.subheader("qtd bolsas")
    st.markdown("""Calcula a quantidade de bolsas concedidas através da contagem de linhas, já que cada linha 
    representa uma bolsa.""")
    st.code("qtd bolsas = COUNTROWS(prouni_2021_2025)")

    st.subheader("qtd deficientes")
    st.markdown("Calcula a quantidade de bolsistas com alguma deficiência física.")
    st.code(f'''qtd deficientes = CALCULATE([qtd bolsas],prouni_2021_2025[BENEFICIARIO_DEFICIENTE_FISICO] = "Sim"''')

    st.subheader(f"% bolsista sexo")
    st.markdown("Calcula qual a porcentagem de bolsistas em cada Sexo.")
    st.code(f"% bolsista sexo = DIVIDE([qtd bolsas],CALCULATE([qtd bolsas],ALL(prouni_2021_2025[SEXO_BENEFICIARIO])))")

    st.subheader(f"% deficientes")
    st.markdown("Calcula qual o percentual de bolsistas com deficiência em relação ao total geral de bolsistas.")
    st.code(f"% deficientes = [qtd deficientes]/[qtd bolsas]")

    st.subheader("avg idade")
    st.markdown("Calcula a idade média dos beneficiários que tiveram bolsas concedidas.")
    st.code(f"avg_idade = AVERAGE(prouni_2021_2025[idade])")

    st.subheader("var ano anterior")
    st.markdown("""Calcula a porcentagem de variação entre o ano atual do filtro selecionado e o ano anterior ao mesmo.""")
    st.code("""var ano anterior = 
                VAR AnoAtual = SELECTEDVALUE(prouni_2021_2025[ANO_CONCESSAO_BOLSA])

                VAR ValorAtual = [qtd bolsas]

                VAR ValorAnterior =
                    CALCULATE([qtd bolsas],FILTER(ALL(prouni_2021_2025[ANO_CONCESSAO_BOLSA]),
                                                        prouni_2021_2025[ANO_CONCESSAO_BOLSA] = AnoAtual - 1))

                RETURN
                    IF(ISBLANK(AnoAtual), BLANK(), DIVIDE(ValorAtual - ValorAnterior,ValorAnterior))""")   

st.subheader("Tooltips criados (Dica de Ferramenta)")
with st.container(border=True):
    st.badge("Essa parte da documentação está sendo terminada!",color="yellow")