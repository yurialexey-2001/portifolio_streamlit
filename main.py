import streamlit as st

st.set_page_config(layout="wide",
                   initial_sidebar_state="expanded")
pages = st.navigation({ 
    
    "GERAL":[st.Page("pages/geral/sobre_mim.py",title="Início",icon="🧑‍🦰")],
                    
    "PROJETOS":
        #PAGINAS INICIAIS
        [st.Page("pages/excel/home_excel.py",title="Projetos de Excel",icon="📈"),
         st.Page("pages/python/home_python.py",title="Projetos de Python",icon="💻"),
         st.Page("pages/sql/home_sql.py",title="Projetos de SQL",icon="🔢"),
         st.Page("pages/power_bi/home_pbi.py",title="Projetos de Power BI",icon="📊"),

         #PROJETOS DO EXCEL
         st.Page("pages/excel/dashboard_vendas.py",title="Dashboard de Vendas",visibility="hidden"),
         st.Page("pages/excel/dashboard_import.py",title="Dashboard de Importação",visibility="hidden"),

         #PROJETOS DO PYTHON
         st.Page("pages/python/cotacao_api.py",title="Cotação de Moedas",visibility="hidden"),
         st.Page("pages/python/cotacao_api_doc.py",title="Documentação do Projeto",visibility="hidden"),

         #PROJETOS DO POWER BI
         st.Page("pages/power_bi/analise_prouni.py",title="Analise Prouni",visibility="hidden"),
         st.Page("pages/power_bi/analise_prouni_doc.py",title="Documentação do Projeto",visibility="hidden")

        #PROJETOS DO SQL
        #AINDA NÃO TEM NADA :(
        ]})

pages.run()



