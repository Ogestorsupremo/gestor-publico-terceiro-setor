import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Gestor Público - Terceiro Setor", layout="wide")

# Título e descrição inicial
st.title("🚀 Gestor Público do Terceiro Setor")
st.subheader("Ferramenta colaborativa para gestão eficiente de projetos sociais")

st.markdown("""
Bem-vindo(a) ao nosso aplicativo! Aqui você pode:

- ✅ Organizar projetos
- 📊 Controlar finanças
- 🧠 Centralizar dados de gestão
- 👥 Trabalhar de forma colaborativa com até 4 pessoas em tempo real

---

### 🔧 Funcionalidades principais (em desenvolvimento):

- Gestão de cadastros de projetos
- Controle de voluntários
- Relatórios financeiros
- Painéis interativos

---

🛠️ Este é o primeiro protótipo. Em breve, mais funcionalidades!
""")

# 🔎 Scanner de Oportunidades - Editais Públicos
st.header("📑 Scanner de Oportunidades - Editais Públicos")
st.write("Busque oportunidades de transferência voluntária da União e outros órgãos públicos.")

# Botão para buscar editais
if st.button("🔍 Buscar Editais Disponíveis"):
    # Dados simulados (iremos substituir por dados reais depois)
    dados_editais = [
        {
            "Órgão": "Ministério da Saúde",
            "Título": "Apoio a Ações na Atenção Básica",
            "Valor": "R$ 500.000,00",
            "Data Limite": "30/06/2025",
            "Link": "https://www.transferegov.gov.br"
        },
        {
            "Órgão": "FNDE",
            "Título": "Reforma de Escolas Municipais",
            "Valor": "R$ 1.200.000,00",
            "Data Limite": "15/07/2025",
            "Link": "https://www.fnde.gov.br"
        },
        {
            "Órgão": "Ministério da Cultura",
            "Título": "Fomento à Cultura em Pequenos Municípios",
            "Valor": "R$ 350.000,00",
            "Data Limite": "05/08/2025",
            "Link": "https://www.transferegov.gov.br"
        },
    ]

    df = pd.DataFrame(dados_editais)

    # Mostrar a tabela
    st.subheader("📋 Editais Encontrados")
    st.dataframe(df, use_container_width=True)

    st.success("Busca concluída! ✅")

else:
    st.info("Clique no botão acima para buscar editais disponíveis.")
