import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Dados médios dos indicadores por ano ===
dados_imobiliario = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],

    'Margem Líquida_2022': [19.99, 21.96, 15.86, 30.51, 1.26, 42.80],
    'Margem Líquida_2023': [128.82, 9.80, 17.68, 22.72, 26.70, 50.28],
    'Margem Líquida_2024': [29.64, 6.02, 24.12, 27.47, 32.34, 52.70],

    'Grau de Endividamento_2022': [35.88, 76.61, 53.51, 17.97, 48.96, 39.48],
    'Grau de Endividamento_2023': [45.39, 76.07, 51.07, 19.97, 46.80, 39.92],
    'Grau de Endividamento_2024': [48.20, 76.31, 53.16, 24.49, 46.38, 54.88],

    'ROE_2022': [2.82, 35.63, 11.15, 7.54, 0.31, 11.69],
    'ROE_2023': [23.13, 14.18, 13.01, 5.23, 7.40, 14.72],
    'ROE_2024': [5.74, 9.37, 19.31, 8.78, 9.57, 23.75],

    'P/L_2022': [18.6, 4.9, 5.8, 7.9, 419.7, 16.1],
    'P/L_2023': [4.0, 13.8, 8.5, 15.5, 22.1, 16.7],
    'P/L_2024': [11.9, 15.7, 3.4, 5.5, 17.1, 8.2],

    'P/VPA_2022': [0.52, 4.9, 0.64, 0.6, 1.31, 1.88],
    'P/VPA_2023': [0.92, 13.8, 1.1, 0.81, 1.63, 2.46],
    'P/VPA_2024': [0.69, 15.7, 0.65, 0.49, 1.64, 1.94],

    'EBITDA_2022': [60.44, 60.90, 18.04, 22.44, 64.33, 70.94],
    'EBITDA_2023': [224.80, 40.47, 19.45, 19.28, 68.83, 75.31],
    'EBITDA_2024': [75.62, 32.16, 26.27, 23.02, 72.41, 72.62],

    'Dividend Yield_2022': [3.72, 4.11, 3.87, 2.85, 0.65, 3.39],
    'Dividend Yield_2023': [7.18, 3.05, 3.73, 1.49, 2.65, 3.40],
    'Dividend Yield_2024': [5.28, 2.07, 8.45, 10.38, 3.25, 4.93],

    'Liquidez Corrente_2022': [3.22, 1.17, 2.48, 4.91, 1.27, 1.37],
    'Liquidez Corrente_2023': [1.79, 1.30, 2.83, 6.24, 2.13, 1.42],
    'Liquidez Corrente_2024': [1.89, 1.70, 3.27, 6.84, 2.16, 1.43],

    'Composição do Endividamento_2022': [23.04, 27.80, 41.78, 47.82, 43.34, 30.16],
    'Composição do Endividamento_2023': [17.02, 20.41, 38.94, 34.29, 24.97, 30.44],
    'Composição do Endividamento_2024': [17.22, 13.60, 32.79, 24.15, 24.87, 22.49],
}
dados_energia = {
    'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
    'Liquidez Corrente_2022': [2.45, 3.06, 1.3, 1.25, 1.2],
    'Liquidez Corrente_2023': [2.46, 2.01, 1.47, 1.46, 0.91],
    'Liquidez Corrente_2024': [2.98, 1.23, 1.26, 0.99, 0.86],
    
    'Margem Líquida_2022': [46.53, 55.39, 5.24, 22.38, 11.88],
    'Margem Líquida_2023': [44.60, 40.70, 10.83, 31.90, 15.65],
    'Margem Líquida_2024': [42.74, 45.56, 12.36, 38.35, 17.88],
    
    'Grau de Endividamento_2022': [50.46, 62.61, 57.49, 77.90, 59.41],
    'Grau de Endividamento_2023': [53.65, 66.27, 56.66, 76.75, 55.17],
    'Grau de Endividamento_2024': [50.24, 66.03, 55.32, 75.49, 54.15],
    
    'EBITDA_2022': [64.54, 94.26, 18.92, 57.03, 19.33],
    'EBITDA_2023': [63.83, 69.97, 23.64, 67.78, 23.08],
    'EBITDA_2024': [64.88, 77.68, 24.41, 78.03, 28.26],
    
    'ROE_2022': [16.26, 22.59, 5.44, 31.57, 18.80],
    'ROE_2023': [17.70, 20.97, 9.62, 34.93, 23.39],
    'ROE_2024': [11.50, 24.41, 10.92, 35.04, 26.00],
    
    'Dividend Yield_2022': [4.83, 15.18, 12.29, 9.01, 12.67],
    'Dividend Yield_2023': [8.59, 10.05, 3.63, 7.59, 16.27],
    'Dividend Yield_2024': [9.08, 9.63, 4.79, 7.88, 14.66],
    
    'P/L_2022': [5.8, 6.9, 17.0, 10.2, 4.3],
    'P/L_2023': [4.8, 8.8, 12.3, 10.1, 3.3],
    'P/L_2024': [8.69, 6.7, 9.3, 6.7, 4.9],
    
    'P/VPA_2022': [0.88, 1.57, 0.93, 3.21, 0.81],
    'P/VPA_2023': [0.95, 1.84, 1.18, 3.54, 0.78],
    'P/VPA_2024': [0.85, 1.64, 1.02, 2.36, 1.28],
    
    'Composição do Endividamento_2022': [8.23, 9.51, 25.05, 19.80, 35.14],
    'Composição do Endividamento_2023': [13.49, 13.76, 29.43, 18.86, 43.15],
    'Composição do Endividamento_2024': [14.05, 18.25, 32.58, 19.22, 43.74]
}

# === Normalização com ponderação de anos ===
def processar_dados(dados):
    df = pd.DataFrame(dados)

    peso_anos = [0.20, 0.35, 0.45]
    indicadores = ['Liquidez Corrente', 'Margem Líquida', 'Grau de Endividamento', 
                   'EBITDA', 'ROE', 'Dividend Yield', 'P/L', 'P/VPA', 'Composição do Endividamento']

    for ind in indicadores:
        df[ind] = (
            df[f'{ind}_2022'] * peso_anos[0] +
            df[f'{ind}_2023'] * peso_anos[1] +
            df[f'{ind}_2024'] * peso_anos[2]
        )

    maior_melhor = ['Liquidez Corrente', 'Margem Líquida', 'ROE', 'Dividend Yield', 'EBITDA']
    menor_melhor = ['Grau de Endividamento', 'Composição do Endividamento', 'P/L', 'P/VPA']

    for col in maior_melhor:
        df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    for col in menor_melhor:
        df[col + '_norm'] = 1 - (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    pesos = {
        'ROE_norm': 0.12,
        'Margem Líquida_norm': 0.12,
        'EBITDA_norm': 0.14,
        'Composição do Endividamento_norm': 0.11,
        'Dividend Yield_norm': 0.10,
        'Grau de Endividamento_norm': 0.09,
        'Liquidez Corrente_norm': 0.07,
        'P/L_norm': 0.10,
        'P/VPA_norm': 0.15
    }

    df['Score Final'] = sum(df[col] * peso for col, peso in pesos.items())
    df_ranked = df[['Empresa', 'Score Final']].sort_values(by='Score Final', ascending=False).reset_index(drop=True)
    return df, df_ranked

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Ranking das Empresas", layout="centered")

st.title("📊 Ranking de Empresas por Setor")
setor = st.selectbox("Selecione o setor:", ["Imobiliário", "Energia"])

if setor == "Imobiliário":
    df, df_ranked = processar_dados(dados_imobiliario)
    dados_base = pd.DataFrame(dados_imobiliario)
    titulo_setor="🧠 Visão Geral do Setor Imobiliário"
    texto_setor="""
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

    Os indicadores foram normalizados e ponderados por ano. Atribuímos pesos com base na relevância para análise do setor:
    - 0.12 para **ROE**, **Margem**, **Composição do Endividamento**
    - 0.14 para **EBITDA**, 0.10 para **Dividend Yield**, 0.09 para **Grau de Endividamento**
    - 0.07 para **Liquidez Corrente**, 0.10 para **P/L**, 0.15 para **P/VPA**

    ### 🏆 Construção do Ranking

    O ranking foi elaborado com base no **score final**, calculado pela média ponderada dos indicadores normalizados. As empresas foram ordenadas do maior para o menor score, identificando as mais eficientes sob a ótica contábil e de mercado.

    ---
    """
else:
    df, df_ranked = processar_dados(dados_energia)
    dados_base = pd.DataFrame(dados_energia)
    titulo_setor = "🧠 Visão Geral do Setor de Energia"
    texto_setor = """
    O setor de energia engloba todas as atividades relacionadas à geração, transmissão, distribuição e comercialização de energia, incluindo energia elétrica, petróleo, gás natural e outros combustíveis.

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

    Os indicadores foram normalizados e ponderados por ano. Atribuímos pesos com base na relevância para análise do setor:
    - 0.12 para **ROE**, **Margem**, **Composição do Endividamento**
    - 0.14 para **EBITDA**, 0.10 para **Dividend Yield**, 0.09 para **Grau de Endividamento**
    - 0.07 para **Liquidez Corrente**, 0.10 para **P/L**, 0.15 para **P/VPA**

    ### 🏆 Construção do Ranking

    O ranking foi elaborado com base no **score final**, calculado pela média ponderada dos indicadores normalizados. As empresas foram ordenadas do maior para o menor score, identificando as mais eficientes sob a ótica contábil e de mercado.
    """

# Exibição das abas
aba0, aba1, aba2, aba3, aba4 = st.tabs(["📘 Introdução", "🏗️ Indicadores", "🏆 Ranking Final", "📈 Gráfico", "📋 Critérios de Avaliação"])

with aba0:
    st.subheader(titulo_setor)
    st.markdown(texto_setor)

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

with aba4:
    st.subheader("📋 Critérios e Distribuição dos Pesos")

    st.markdown("### 📅 Peso dos Indicadores por Ano")
    dados_ano = pd.DataFrame({
        "Ano": ["2024", "2023", "2022"],
        "Peso": ["45%", "35%", "20%"]
    })
    st.dataframe(dados_ano, use_container_width=True, hide_index=True)

    st.markdown("### 🧮 Distribuição por Tipo de Medição")
    dados_tipo = pd.DataFrame({
        "Tipo de Medição": ["Rentabilidade", "Dívida", "Valuation"],
        "Porcentagem": ["38%", "27%", "35%"]
    })
    st.dataframe(dados_tipo, use_container_width=True, hide_index=True)

    st.markdown("### ⚖️ Pesos dos Indicadores")
    dados_indicadores = pd.DataFrame({
        "Índices": [
            "Índices Contábeis", "", "", "", "", "", "Total Contábeis",
            "Índices de Bolsa", "", "", "Bolsa Total"
        ],
        "Indicadores": [
            "ROE", "Margem Líquida", "MARGEM EBITDA", "Composição do Endividamento",
            "Grau de Endividamento", "Liquidez Corrente", "",
            "P/L", "P/VPA", "Rendimento de Dividendos", ""
        ],
        "Pesos": [
            "0,12", "0,12", "0,14", "0,11", "0,09", "0,07", "0,65",
            "0,10", "0,15", "0,10", "0,35"
        ],
        "Tipo de Medição": [
            "Rentabilidade", "Rentabilidade", "Rentabilidade",
            "Dívida", "Dívida", "Dívida", "",
            "Avaliação", "Avaliação", "Avaliação", ""
        ]
    })
    st.dataframe(dados_indicadores, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Projeto de análise desenvolvido com Streamlit | Dados para uso acadêmico")