import streamlit as st

st.set_page_config(layout="wide",
                   initial_sidebar_state="expanded")
pages = st.navigation({ 
    
    "Geral":[st.Page("pages/geral/sobre_mim.py",title="Início",icon="🧑‍🦰")],
                    
    "PROJETOS":
        [st.Page("pages/excel/home_excel.py",title="Projetos de Excel",icon="📈"),
         st.Page("pages/python/home_python.py",title="Projetos de Python",icon="💻"),
         st.Page("pages/sql/home_sql.py",title="Projetos de SQL",icon="🔢"),
         st.Page("pages/power_bi/home_pbi.py",title="Projetos de Power BI",icon="📊"),
         st.Page("pages/excel/dashboard_vendas.py",title="Dashboard de Vendas",visibility="hidden"),
         st.Page("pages/excel/dashboard_import.py",title="Dashboard de Importacao",visibility="hidden"),
         st.Page("pages/python/cotacao_api.py",title="cotacao",visibility="hidden"),
         st.Page("pages/python/cotacao_api_doc.py",title="Doc_cotacao",visibility="hidden")]})

pages.run()



