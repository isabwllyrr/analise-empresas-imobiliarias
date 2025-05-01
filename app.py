
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Dados médios dos indicadores (2022-2024) ===
dados = {
    'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
    'Liquidez Corrente': [2.30, 1.39, 2.86, 6.00, 1.85, 1.41],
    'Grau de Endividamento': [43.16, 76.33, 52.58, 20.81, 47.38, 44.76],
    'Margem Líquida': [59.48, 12.59, 19.22, 26.90, 20.10, 48.59],
    'ROE': [10.56, 19.73, 14.49, 7.18, 5.76, 16.72],
    'P/L': [11.50, 11.47, 5.90, 9.63, 152.97, 13.67],
    'P/VPA': [0.71, 11.47, 0.80, 0.63, 1.53, 2.09],
    'Dividend Yield': [5.39, 3.08, 5.35, 4.91, 2.18, 3.91]
}

df = pd.DataFrame(dados)

# Normalização
maior_melhor = ['Liquidez Corrente', 'Margem Líquida', 'ROE', 'Dividend Yield']
menor_melhor = ['Grau de Endividamento', 'P/L', 'P/VPA']

for col in maior_melhor:
    df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

for col in menor_melhor:
    df[col + '_norm'] = 1 - (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Pesos
pesos = {
    'Liquidez Corrente_norm': 0.10,
    'Grau de Endividamento_norm': 0.15,
    'Margem Líquida_norm': 0.15,
    'ROE_norm': 0.15,
    'P/L_norm': 0.15,
    'P/VPA_norm': 0.10,
    'Dividend Yield_norm': 0.10
}

# Score final
df['Score Final'] = sum(df[col] * peso for col, peso in pesos.items())
df_ranked = df[['Empresa', 'Score Final']].sort_values(by='Score Final', ascending=False).reset_index(drop=True)

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Ranking Imobiliário", layout="centered")

st.title("📊 Ranking de Empresas do Setor Imobiliário")

aba1, aba2, aba3 = st.tabs(["🏗️ Indicadores", "🏆 Ranking Final", "📈 Gráfico"])

with aba1:
    st.subheader("📌 Indicadores Médios por Empresa (2022-2024)")
    st.dataframe(df[dados.keys()].set_index('Empresa'), use_container_width=True)
    st.markdown("Indicadores como Liquidez, Endividamento, Margem e ROE foram utilizados com pesos ponderados para construir o ranking final.")

with aba2:
    st.subheader("🏆 Ranking Final (Score Normalizado)")
    st.dataframe(df_ranked, use_container_width=True)
    st.markdown("O Score é resultado da média ponderada dos indicadores normalizados.")

with aba3:
    st.subheader("📈 Gráfico de Ranking Final")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df_ranked['Empresa'], df_ranked['Score Final'], color='#66b3ff', edgecolor='black')
    ax.set_title("Ranking Final das Empresas (Score)", fontsize=14)
    ax.set_ylabel("Score Normalizado")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

st.markdown("---")
st.caption("Projeto de análise desenvolvido com Streamlit | Dados fictícios de exemplo para uso acadêmico")
