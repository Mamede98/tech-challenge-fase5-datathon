import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Configuração da Página
st.set_page_config(page_title="Passos Mágicos - Previsão de Risco", page_icon="🔮", layout="centered")

# Título e Descrição
st.image("app/Passos-magicos-icon-cor.png", width=200)
st.title("Sistema de Alerta Educacional 🚨")
st.markdown("""
    <p style='font-size: 14px;'>
        Este sistema utiliza um modelo preditivo de Machine Learning para antecipar o 
        risco de defasagem escolar, cruzando indicadores acadêmicos e comportamentais 
        para apoiar a equipe pedagógica.
    </p> 
            
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    div.stButton > button:first-child {
        background-color: #004b87; /* Cor de fundo */
        color: white; /* Cor da letra */
        border-radius: 10px; /* Bordas arredondadas */
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Sombra elegante */
        font-weight: bold;
        transition: all 0.3s ease 0s;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #003366;
        transform: translateY(-2px); /* Efeito de 'levantar' o botão */
    }

    div[data-baseweb="input"] {
        border-radius: 8px !important;
    }
            
    [data-testid="stMetricValue"] {
        font-size: 1.8rem !important; /* O padrão é quase 3rem. Vá diminuindo até caber! */
    }              
    </style>
""", unsafe_allow_html=True)

# Carregando o Modelo Treinado
@st.cache_resource
def carregar_modelo():
    return joblib.load('app/modelo_pede.pkl')

modelo = carregar_modelo()

st.divider()
st.subheader("📊 Insira os Dados do Aluno")

col1, col2 = st.columns(2)

with col1:
    fase = st.number_input("Fase Atual do Aluno (0 a 8)", min_value=0, max_value=8, value=3)
    ida = st.slider("Nota IDA (Desempenho Acadêmico)", 0.0, 10.0, 5.0, 0.1)
    ipp = st.slider("Nota IPP (Psicopedagógico)", 0.0, 10.0, 5.0, 0.1)

with col2:
    ipv = st.slider("Nota IPV (Ponto de Virada)", 0.0, 10.0, 5.0, 0.1)
    ieg = st.slider("Nota IEG (Engajamento)", 0.0, 10.0, 5.0, 0.1)
    
    escola = st.selectbox("Vem de Escola Pública?", ["Sim", "Não"])
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])

st.divider()

# Botão de Ação
if st.button("🔍 Analisar Risco do Aluno", type="primary", use_container_width=True):
    
    escola_publica = 1 if escola == "Sim" else 0
    genero_binario = 1 if genero == "Masculino" else 0
    
    dados_entrada = pd.DataFrame([[fase, ieg, ida, ipv, ipp, genero_binario, escola_publica]], 
                                 columns=['fase', 'ieg', 'ida', 'ipv', 'ipp', 'genero_binario', 'escola_publica'])
    
    previsao = modelo.predict(dados_entrada)[0]
    probabilidade = modelo.predict_proba(dados_entrada)[0]
    
    st.subheader("📋 Resultado da Análise:")
    
    if previsao == 1:
        st.error(f"⚠️ **ALERTA: Aluno em Risco de Defasagem!**")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Status", value="Risco Detectado", delta="- Atenção", delta_color="inverse")
        col2.metric(label="Probabilidade", value=f"{probabilidade[1]*100:.1f}%")
        col3.metric(label="Fase Atual", value=f"{fase}")

        st.info("💡 **Ação Sugerida:** Agendar reunião com a equipe pedagógica para intervenção imediata e revisão do Plano de Ensino.")
    else:
        st.success(f"✅ **Aluno Sem Risco de Defasagem**")


        col1, col2, col3 = st.columns(3)
        col1.metric(label="Status", value="Em Fase", delta="Adequado")
        col2.metric(label="Probabilidade de Risco", value=f"{probabilidade[1]*100:.1f}%")
        col3.metric(label="Fase Atual", value=f"{fase}")
        
        st.write("O modelo indica que o aluno está em fase de desenvolvimento saudável. Mantenha o acompanhamento padrão.")