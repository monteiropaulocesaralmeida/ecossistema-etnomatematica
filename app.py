import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Ecossistema Educacional Etnomatemático",
    page_icon="🧮",
    layout="wide"
)

# Título do App
st.title("🧮 Ecossistema Educacional Etnomatemático Libertador")
st.caption("Baseado nos princípios de Ubiratan D'Ambrosio e Paulo Freire | ProfEPT - IFF")

# Sidebar - Seleção de Nível e Navegação
st.sidebar.header("🧭 Navegação e Configuração")
nivel_ensino = st.sidebar.radio("Nível de Ensino:", ["Ensino Médio (ENEM)", "Ensino Fundamental (6º ao 9º)"])
area_enem = st.sidebar.selectbox("Área do Conhecimento (ENEM):", [
    "Matemática e suas Tecnologias",
    "Ciências Humanas e suas Tecnologias",
    "Ciências Da Natureza e suas Tecnologias",
    "Linguagens, Códigos e suas Tecnologias"
])

# Inicialização de Estado para Territórios Dinâmicos
if 'territorios' not in st.session_state:
    st.session_state['territorios'] = {
        "Pesca Artesanal em Atafona e Porto do Açu (SJBB-RJ)": {
            "tema": "Logística, Produção e Economia na Pesca de Atafona",
            "palavras": "Pescado, Barco, Custo, Tabela, Matriz",
            "videos": [
                "https://drive.google.com/file/d/1y51AtIl3qv9JN_xm8B96b4s853QciJSg/view?usp=sharing",
                "https://drive.google.com/file/d/1O05u3yEQ2XnnK2Umh9FnpaxyWJNamgkg/view?usp=sharing",
                "https://drive.google.com/file/d/1Wk4n7oPFIIIZd9jzlRsvG5ljlZ2Tldn0/view?usp=sharing",
                "https://drive.google.com/file/d/1EB47HyikA648SwyeBAwmn7R16_WjibSX/view?usp=sharing",
                "https://drive.google.com/file/d/1kS-cyINCEhd7LKJgfNm27glhPwKrULYh/view?usp=sharing"
            ]
        }
    }

# Seleção de Território
st.subheader("📍 1. Leitura Metodológica do Território")
opcao_territorio = st.selectbox(
    "Selecione ou Adicione uma Realidade/Território de Práxis:",
    list(st.session_state['territorios'].keys()) + ["➕ Cadastrar Novo Território / Realidade (Lavouras, Fábricas, etc.)"]
)

# Cadastro de Novo Território
if opcao_territorio == "➕ Cadastrar Novo Território / Realidade (Lavouras, Fábricas, etc.)":
    with st.form("form_novo_territorio"):
        st.markdown("### 📝 Festa Comunitária Cidadã - Leitura de Mundo")
        novo_nome = st.text_input("Nome da Comunidade / Território (ex: Lavoura de Café do Agreste):")
        novo_tema = st.text_input("Tema Gerador (Levantado na Festa Cidadã):")
        novas_palavras = st.text_input("Palavras Geradoras (separadas por vírgula):")
        diagnostico = st.text_area("Anotações do Diagnóstico Territorial (15 Dimensões):")
        
        btn_salvar = st.form_submit_button("Cadastrar Território")
        if btn_salvar and novo_nome:
            st.session_state['territorios'][novo_nome] = {
                "tema": novo_tema,
                "palavras": novas_palavras,
                "videos": []
            }
            st.success(f"Território '{novo_nome}' adicionado com sucesso!")
            st.rerun()

else:
    dados_t = st.session_state['territorios'][opcao_territorio]
    st.info(f"**Tema Gerador Ativo:** {dados_t['tema']}\n\n**Palavras Geradoras:** {dados_t['palavras']}")

st.divider()

# Módulo Específico: Matrizes e Determinantes
st.subheader("📚 2. Conteúdo Programático: Matrizes e Determinantes")

col1, col2 = st.columns([1, 1])
with col1:
    periodicidade = st.selectbox("Periodicidade do Planejamento:", ["Semanal", "Mensal", "Bimestral", "Trimestral", "Anual"])
with col2:
    qtd_aulas = st.number_input("Carga Horária Total (Horas):", value=5, min_value=1, max_value=80)

# Abas com as 5 Camadas Pedagógicas
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "🎬 1. Vídeos & Avatar IA", 
    "📜 2. História & Etnomatemática", 
    "🔍 3. Aula de Campo", 
    "👥 4. Dinâmicas de Grupo", 
    "🎮 5. Jogos & Tecnologia",
    "📎 Compilador Multimídia"
])

with aba1:
    st.markdown("### Vídeo-aulas Expositivas na Íntegra (Avatar IA + Transcrição)")
    st.write("Links configurados para processamento de voz e avatar:")
    if opcao_territorio in st.session_state['territorios']:
        for idx, link in enumerate(st.session_state['territorios'][opcao_territorio]['videos'], 1):
            st.markdown(f"* **Aula {idx}:** [Acessar Vídeo {idx} no Google Drive]({link})")

with aba2:
    st.markdown("### Dimensão Histórica e Etnomatemática")
    st.write("Análise da origem das tabelas e transposição para o contexto empírico do território selecionado.")

with aba3:
    st.markdown("### Roteiro de Investigação Diagnóstica e Intervenção de Campo")
    st.write("Coleta de dados reais para montagem da matriz de produção/custos da comunidade.")

with aba4:
    st.markdown("### Dinâmicas de Grupo Interativas")
    st.write("Atividades como 'A Malha Humana' para vivenciar as coordenadas e operações matriciais.")

with aba5:
    st.markdown("### Jogos Manipuláveis e Soluções Tecnológicas")
    st.write("Tabuleiro Sarrus com fios coloridos, simulações em planilhas eletrônicas e código Python.")

with aba6:
    st.markdown("### 📎 Repositório Multimídia do Professor")
    st.file_uploader("Adicionar novos PDFs, Imagens ou Documentos ao Módulo:", accept_multiple_files=True)
    st.text_input("Adicionar novo link de vídeo do Google Drive:")
    if st.button("Salvar Materiais no Módulo"):
        st.success("Materiais anexados com sucesso ao planejamento!")
