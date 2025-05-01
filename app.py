import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Dados médios dos indicadores (2022-2024) ===
dados_imobiliario = {
    'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
    'Liquidez Corrente': [2.30, 1.39, 2.86, 6.00, 1.85, 1.41],
    'Grau de Endividamento': [43.16, 76.33, 52.58, 20.81, 47.38, 44.76],
    'Composição do Endividamento': [23.04, 27.80, 41.78, 47.82, 43.34, 30.16],
    'Margem Líquida': [59.48, 12.59, 19.22, 26.90, 20.10, 48.59],
    'ROE': [10.56, 19.73, 14.49, 7.18, 5.76, 16.72],
    'P/L': [11.50, 11.47, 5.90, 9.63, 152.97, 13.67],
    'P/VPA': [0.71, 11.47, 0.80, 0.63, 1.53, 2.09],
    'Dividend Yield': [5.39, 3.08, 5.35, 4.91, 2.18, 3.91],
    'EBITDA': [120.29, 44.51, 21.25, 21.58, 68.52, 72.96]
}

dados_energia = {
    'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
    'Liquidez Corrente': [2.63, 2.1, 1.34, 1.23, 0.99],
    'Grau de Endividamento': [51.45, 64.97, 56.49, 76.71, 56.24],
    'Composição do Endividamento': [11.92, 13.84, 29.02, 19.29, 40.67 ],
    'Margem Líquida': [44.63, 47.22, 9.48, 30.80, 15.14],
    'ROE': [15.15, 22.66, 10.92, 33.85, 22.73],
    'P/L': [6.43, 7.46, 12.86, 9.0, 4.16],
    'P/VPA': [0.89, 1.68, 1.04, 3.04, 0.96],
    'Dividend Yield': [7.50, 11.62, 6.90, 8.16, 14.53],
    'EBITDA': [64.42, 80.64, 22.32, 67.61, 23.56]
}

# === Normalização ===
def processar_dados(dados, setor='geral'):
    df = pd.DataFrame(dados)

    if setor == "imobiliario":
        maior_melhor = ['Liquidez Corrente', 'Margem Líquida', 'ROE', 'Dividend Yield', 'EBITDA']
        menor_melhor = ['Grau de Endividamento', 'Composição do Endividamento', 'P/L', 'P/VPA']

        for col in maior_melhor:
            df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

        for col in menor_melhor:
            df[col + '_norm'] = 1 - (df[col] - df[col].min()) / (df[col].max() - df[col].min())

        pesos = {
            'ROE_norm': 0.15,
            'Margem Líquida_norm': 0.15,
            'EBITDA_norm': 0.15,
            'Composição do Endividamento_norm': 0.12,
            'Dividend Yield_norm': 0.10,
            'Grau de Endividamento_norm': 0.10,
            'Liquidez Corrente_norm': 0.08,
            'P/L_norm': 0.08,
            'P/VPA_norm': 0.07
        }

    else:
        maior_melhor = ['Liquidez Corrente', 'Margem Líquida', 'ROE', 'Dividend Yield']
        menor_melhor = ['Grau de Endividamento', 'P/L', 'P/VPA']

        for col in maior_melhor:
            df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

        for col in menor_melhor:
            df[col + '_norm'] = 1 - (df[col] - df[col].min()) / (df[col].max() - df[col].min())

        pesos = {
            'Liquidez Corrente_norm': 0.10,
            'Grau de Endividamento_norm': 0.15,
            'Margem Líquida_norm': 0.15,
            'ROE_norm': 0.15,
            'P/L_norm': 0.15,
            'P/VPA_norm': 0.10,
            'Dividend Yield_norm': 0.10
        }

    df['Score Final'] = sum(df[col] * peso for col, peso in pesos.items())
    df_ranked = df[['Empresa', 'Score Final']].sort_values(by='Score Final', ascending=False).reset_index(drop=True)
    return df, df_ranked

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Ranking das Empresas", layout="centered")

st.title("📊 Ranking de Empresas por Setor")
setor = st.selectbox("Selecione o setor:", ["Imobiliário", "Energia"])

if setor == "Imobiliário":
    df, df_ranked = processar_dados(dados_imobiliario, setor="imobiliario")
    dados_base = dados_imobiliario
else:
    df, df_ranked = processar_dados(dados_energia)
    dados_base = dados_energia

aba0, aba1, aba2, aba3 = st.tabs(["📘 Introdução", "🏗️ Indicadores", "🏆 Ranking Final", "📈 Gráfico"])

with aba0:
    st.subheader("🧠 Visão Geral do Setor Imobiliário")
    st.markdown("""
    O setor imobiliário é responsável por atividades ligadas à compra, venda, aluguel e construção de imóveis, sendo um dos principais termômetros da economia.

    ### 🔍 Indicadores Utilizados

    Para avaliar o desempenho das empresas, foram escolhidos os seguintes indicadores:
    - **Liquidez Corrente**: capacidade de pagar dívidas de curto prazo.
    - **Grau de Endividamento**: proporção da dívida em relação ao patrimônio.
    - **Composição do Endividamento**: participação do passivo oneroso no total.
    - **Margem Líquida**: lucratividade após despesas operacionais e impostos.
    - **ROE** (Rentabilidade do Patrimônio Líquido): eficiência em gerar lucro com o patrimônio.
    - **P/L** (Preço sobre Lucro): tempo de retorno do investimento.
    - **P/VPA** (Preço sobre Valor Patrimonial): disposição do investidor.
    - **Dividend Yield**: retorno ao acionista via dividendos.
    - **EBITDA**: capacidade operacional de geração de caixa.

    ### ⚖️ Critérios de Normalização e Pesos

    Os indicadores foram normalizados para ficarem entre 0 e 1. Atribuímos pesos com base na relevância para análise do setor:
    - 0.15 para indicadores fundamentais como **ROE**, **Margem**, **Endividamento** e **P/L**
    - 0.10 para **Liquidez**, **P/VPA**, **Yield** e **EBITDA**
    - 0.10 para **Composição do Endividamento**

    ### 🏆 Construção do Ranking

    O ranking foi elaborado com base no **score final**, calculado pela média ponderada dos indicadores normalizados. As empresas foram ordenadas do maior para o menor score, identificando as mais eficientes sob a ótica contábil e de mercado.

    ---
    """)

with aba1:
    st.subheader("📌 Indicadores Médios por Empresa (2022-2024)")
    st.dataframe(pd.DataFrame(dados_base).set_index('Empresa'), use_container_width=True)

with aba2:
    st.subheader("🏆 Ranking Final (Score Normalizado)")
    st.dataframe(df_ranked, use_container_width=True)

with aba3:
    st.subheader("📈 Gráfico de Ranking Final")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df_ranked['Empresa'], df_ranked['Score Final'], color='#66b3ff', edgecolor='black')
    ax.set_title("Ranking Final das Empresas (Score)", fontsize=14)
    ax.set_ylabel("Score Normalizado")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

st.markdown("---")
st.caption("Projeto de análise desenvolvido com Streamlit | Dados para uso acadêmico")
