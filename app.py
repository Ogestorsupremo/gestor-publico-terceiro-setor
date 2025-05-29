import streamlit as st
import pandas as pd
import datetime

# Configuração da página
st.set_page_config(page_title="Gestor Público - Terceiro Setor", layout="wide")

# ----------------------------
# 🚀 Cabeçalho Principal
# ----------------------------
st.title("🚀 Gestor Público do Terceiro Setor")
st.subheader("Ferramenta colaborativa para gestão eficiente de projetos sociais")

st.markdown("""
Bem-vindo(a) ao nosso aplicativo! Aqui você pode:

- ✅ Organizar projetos
- 📊 Controlar finanças
- 🧠 Centralizar dados de gestão
- 👥 Trabalhar de forma colaborativa com até 4 pessoas em tempo real

---

### 🔧 Funcionalidades principais:

1️⃣ Scanner de Editais Públicos  
2️⃣ Análise de Elegibilidade  
3️⃣ Geração de Projeto Simplificado  
4️⃣ Painel de Acompanhamento de Projetos  
5️⃣ Upload e Gestão de Documentos da Entidade  

---
""")

# ----------------------------
# 🔎 Scanner de Oportunidades
# ----------------------------
st.header("📑 Scanner de Oportunidades - Editais Públicos")
st.write("Busque oportunidades de transferência voluntária da União e outros órgãos públicos.")

if st.button("🔍 Buscar Editais Disponíveis"):
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
    st.subheader("📋 Editais Encontrados")
    st.dataframe(df, use_container_width=True)
    st.success("Busca concluída! ✅")
else:
    st.info("Clique no botão acima para buscar editais disponíveis.")

st.divider()

# ----------------------------
# 🧠 Análise de Elegibilidade
# ----------------------------
st.header("🧠 Análise de Elegibilidade da Entidade")

cnpj = st.text_input("Informe o CNPJ da entidade (somente números)")

if st.button("🚦 Verificar Elegibilidade"):
    if cnpj.strip() == "":
        st.warning("Por favor, informe um CNPJ válido.")
    else:
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

st.divider()

# ----------------------------
# 📝 Geração de Projeto
# ----------------------------
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

st.divider()

# ----------------------------
# 📊 Painel de Acompanhamento
# ----------------------------
st.header("📊 Painel de Acompanhamento de Projetos")

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

df_painel = pd.DataFrame(dados_projetos)

st.subheader("📋 Status dos Projetos")
st.dataframe(df_painel, use_container_width=True)

st.info("🚦 Acompanhe os projetos e seus respectivos status.")

st.divider()

# ----------------------------
# 📂 Gestão de Documentos
# ----------------------------
st.header("📂 Gestão de Documentos da Entidade")
st.subheader("Organize e envie documentos essenciais para habilitação da entidade.")

st.markdown("""
Envie aqui documentos importantes da sua organização, como:

- 🏛️ Estatuto Social
- 📝 Ata de Constituição
- ✅ Certidões Negativas
- 📄 Declarações
- 📑 Outros documentos obrigatórios
""")

if 'arquivos' not in st.session_state:
    st.session_state['arquivos'] = []

st.subheader("⬆️ Envio de Documentos")
arquivo = st.file_uploader("Selecione um arquivo", type=['pdf', 'jpg', 'png', 'docx'])
descricao = st.text_input("Descrição do documento (ex.: Estatuto Social, Certidão, etc.)")

if st.button("📤 Enviar Documento"):
    if arquivo is not None and descricao.strip() != "":
        st.session_state['arquivos'].append({
            "Nome": arquivo.name,
            "Descrição": descricao,
            "Data Upload": datetime.datetime.now().strftime('%d/%m/%Y %H:%M'),
            "Arquivo": arquivo
        })
        st.success(f"✅ Documento '{arquivo.name}' enviado com sucesso!")
    else:
        st.warning("Por favor, selecione um arquivo e preencha a descrição.")

st.subheader("📜 Documentos Enviados")

if len(st.session_state['arquivos']) > 0:
    df_arquivos = pd.DataFrame([{
        "Nome": item['Nome'],
        "Descrição": item['Descrição'],
        "Data Upload": item['Data Upload']
    } for item in st.session_state['arquivos']])

    st.dataframe(df_arquivos, use_container_width=True)

    for idx, item in enumerate(st.session_state['arquivos']):
        with st.expander(f"📄 {item['Nome']}"):
            st.write(f"**Descrição:** {item['Descrição']}")
            st.write(f"**Enviado em:** {item['Data Upload']}")
            st.download_button(
                label="⬇️ Baixar Arquivo",
                data=item['Arquivo'].getvalue(),
                file_name=item['Nome']
            )
            if st.button(f"🗑️ Remover '{item['Nome']}'", key=f"remove_{idx}"):
                st.session_state['arquivos'].pop(idx)
                st.success(f"Documento '{item['Nome']}' removido.")
                st.experimental_rerun()
else:
    st.info("Nenhum documento enviado até o momento.")
