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

# 🔍 Análise de Elegibilidade
st.header("🧠 Análise de Elegibilidade da Entidade")

cnpj = st.text_input("Informe o CNPJ da entidade (somente números)")

if st.button("🚦 Verificar Elegibilidade"):
    if cnpj.strip() == "":
        st.warning("Por favor, informe um CNPJ válido.")
    else:
        # 🔗 Simulação de checagem (iremos integrar APIs depois)
        st.subheader("🔍 Resultado da Análise:")

        resultado = {
            "CNPJ Ativo na Receita Federal": "✅ Regular",
            "Situação no CAUC": "❌ Irregular - Pendências Financeiras",
            "Certidão Negativa Federal": "✅ Regular",
            "Certidão Estadual": "✅ Regular",
            "Observações": "⚠️ Resolver pendências no CAUC para avançar com projetos públicos."
        }

        resultado_df = pd.DataFrame(list(resultado.items()), columns=["Item", "Status"])
        st.table(resultado_df)

        if "❌" in "".join(resultado.values()):
            st.error("⚠️ A entidade possui pendências. Recomenda-se resolver antes de submeter projetos.")
        else:
            st.success("✅ Tudo certo! A entidade está apta para receber recursos públicos.")
# 📝 Geração de Projeto Simplificado
st.header("📑 Geração Automática de Projeto")

nome_projeto = st.text_input("Título do Projeto")
area_atuacao = st.selectbox("Área de Atuação", ["Educação", "Saúde", "Assistência Social", "Cultura", "Esporte", "Outros"])
valor_projeto = st.number_input("Valor Total do Projeto (R$)", min_value=1000.0, step=1000.0)

if st.button("🚀 Gerar Projeto"):
    if nome_projeto.strip() == "":
        st.warning("Por favor, preencha o título do projeto.")
    else:
        st.subheader(f"📄 Projeto: {nome_projeto}")

        st.markdown(f"""
        ### 🩺 Diagnóstico
        Há uma necessidade significativa na área de **{area_atuacao}**, onde a comunidade local enfrenta desafios constantes que comprometem sua qualidade de vida. Este projeto busca mitigar tais dificuldades através de ações estruturadas.

        ### 📜 Justificativa
        A implementação deste projeto visa promover melhorias na área de **{area_atuacao}**, atendendo diretamente a população e fortalecendo as políticas públicas locais. Considera-se também os Objetivos de Desenvolvimento Sustentável (ODS) alinhados às diretrizes governamentais.

        ### 🎯 Objetivos
        - Promover ações voltadas para melhoria da **{area_atuacao}**.
        - Fortalecer a atuação do terceiro setor na região.
        - Contribuir com o desenvolvimento social e econômico.

        ### 🗂️ Plano de Trabalho
        - **Meta 1:** Início das atividades de mobilização comunitária.
        - **Meta 2:** Execução das atividades técnicas e operacionais.
        - **Meta 3:** Acompanhamento e avaliação de resultados.

        ### 📅 Cronograma
        - **Mês 1:** Planejamento e mobilização.
        - **Mês 2-5:** Execução das ações.
        - **Mês 6:** Avaliação e prestação de contas.

        ### 💰 Orçamento Total
        **R$ {valor_projeto:,.2f}**

        ### 🏛️ Termo de Referência (Simplificado)
        - Objeto: Execução do projeto "{nome_projeto}" na área de **{area_atuacao}**.
        - Justificativa: Atender demandas da comunidade, conforme diagnóstico.
        - Valor estimado: R$ {valor_projeto:,.2f}.
        - Vigência: 6 meses.

        ---
        ✅ Documento gerado automaticamente. Personalize conforme necessidade.
        """)

        st.success("🚀 Projeto gerado com sucesso!")

# 📊 Painel de Acompanhamento de Projetos
st.header("📊 Painel de Acompanhamento de Projetos")

# Dados simulados para teste (substituir depois por banco de dados real)
dados_projetos = [
    {
        "Projeto": "Apoio à Saúde Municipal",
        "Status": "Em Execução",
        "Valor (R$)": 500000,
        "Data Limite": "30/06/2025"
    },
    {
        "Projeto": "Reforma de Escolas Municipais",
        "Status": "Aprovado",
        "Valor (R$)": 1200000,
        "Data Limite": "15/07/2025"
    },
    {
        "Projeto": "Fomento à Cultura Local",
        "Status": "Prestação de Contas",
        "Valor (R$)": 350000,
        "Data Limite": "05/08/2025"
    }
]

import pandas as pd

df_painel = pd.DataFrame(dados_projetos)

st.subheader("📋 Status dos Projetos")
st.dataframe(df_painel, use_container_width=True)

st.info("🚦 Acompanhe os projetos e seus respectivos status.")
