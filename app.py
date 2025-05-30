import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# testando os graficos da margem liquida 
def plot_margem_liquida_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [19.99, 21.96, 15.86, 30.51, 1.26, 42.80],
        '2023': [128.82, 9.80, 17.68, 22.72, 26.70, 50.28],
        '2024': [29.64, 6.02, 24.12, 27.47, 32.34, 52.70],
        'Média': [59.48, 12.59, 19.22, 26.90, 20.10, 48.59]
    }
    df = pd.DataFrame(dados)
    media_global = 23.50

    empresas = df['Empresa']
    m2022 = df['2022']
    m2023 = df['2023']
    m2024 = df['2024']
    media = df['Média']

    fig, ax = plt.subplots(figsize=(12, 6))
    width = 0.25
    x = range(len(empresas))

    ax.bar([p - width for p in x], m2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, m2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], m2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)

    ax.axhline(media_global, color='#ff4500', linestyle='--', label='Média Global (23,50%)', linewidth=2)

    ax.set_title("Margem Líquida das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Margem Líquida (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')

    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_grau_endividamento_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [35.88, 76.61, 53.51, 17.97, 48.96, 39.48],
        '2023': [45.39, 76.07, 51.07, 19.97, 46.80, 39.92],
        '2024': [48.20, 76.31, 53.16, 24.49, 46.38, 54.88],
        'Média': [43.16, 76.33, 52.58, 20.81, 47.38, 44.76]
    }
    df = pd.DataFrame(dados)
    media_global = 47.17

    empresas = df['Empresa']
    d2022, d2023, d2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], d2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, d2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], d2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f}%)', linewidth=2)

    ax.set_title("Grau de Endividamento das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Endividamento (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_roe_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [2.82, 35.63, 11.15, 7.54, 0.31, 11.69],
        '2023': [23.13, 14.18, 13.01, 5.23, 7.40, 14.72],
        '2024': [5.74, 9.37, 19.31, 8.78, 9.57, 23.75],
        'Média': [10.56, 19.73, 14.49, 7.18, 5.76, 16.72]
    }
    df = pd.DataFrame(dados)
    media_global = 12.07

    empresas = df['Empresa']
    r2022, r2023, r2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], r2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, r2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], r2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f}%)', linewidth=2)

    ax.set_title("ROE das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("ROE (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_pl_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [18.6, 4.9, 5.8, 7.9, 419.7, 16.1],
        '2023': [4.0, 13.8, 8.5, 15.5, 22.1, 16.7],
        '2024': [11.9, 15.7, 3.4, 5.5, 17.1, 8.2],
        'Média': [11.5, 11.47, 5.9, 9.63, 152.97, 13.67]
    }
    df = pd.DataFrame(dados)
    media_global = 34.19

    empresas = df['Empresa']
    p2022, p2023, p2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], p2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, p2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], p2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f})', linewidth=2)

    ax.set_title("P/L das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("P/L")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_pvpa_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [0.52, 4.9, 0.64, 0.6, 1.31, 1.88],
        '2023': [0.92, 13.8, 1.1, 0.81, 1.63, 2.46],
        '2024': [0.69, 15.7, 0.65, 0.49, 1.64, 1.94],
        'Média': [0.71, 11.47, 0.80, 0.63, 1.53, 2.09]
    }
    df = pd.DataFrame(dados)
    media_global = 2.87

    empresas = df['Empresa']
    v2022, v2023, v2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], v2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, v2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], v2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f})', linewidth=2)

    ax.set_title("P/VPA das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("P/VPA")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_ebitda_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [60.44, 60.90, 18.04, 22.44, 64.33, 70.94],
        '2023': [224.80, 40.47, 19.45, 19.28, 68.83, 75.31],
        '2024': [75.62, 32.16, 26.27, 23.02, 72.41, 72.62],
        'Média': [120.29, 44.51, 21.25, 21.58, 68.52, 72.96]
    }
    df = pd.DataFrame(dados)
    media_global = 58.52

    empresas = df['Empresa']
    e2022, e2023, e2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], e2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, e2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], e2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f})', linewidth=2)

    ax.set_title("EBITDA das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("EBITDA (R$ mi)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_dividend_yield_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [3.72, 4.11, 3.87, 2.85, 0.65, 3.39],
        '2023': [7.18, 3.05, 3.73, 1.49, 2.65, 3.40],
        '2024': [5.28, 2.07, 8.45, 10.38, 3.25, 4.93],
        'Média': [5.39, 3.08, 5.35, 4.91, 2.18, 3.91]
    }
    df = pd.DataFrame(dados)
    media_global = 4.47

    empresas = df['Empresa']
    y2022, y2023, y2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], y2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, y2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], y2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f}%)', linewidth=2)

    ax.set_title("Dividend Yield das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Dividend Yield (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_liquidez_corrente_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [3.22, 1.17, 2.48, 4.91, 1.27, 1.37],
        '2023': [1.79, 1.30, 2.83, 6.24, 2.13, 1.42],
        '2024': [1.89, 1.70, 3.27, 6.84, 2.16, 1.43],
        'Média': [2.30, 1.39, 2.86, 6.00, 1.85, 1.41]
    }
    df = pd.DataFrame(dados)
    media_global = 2.97

    empresas = df['Empresa']
    l2022, l2023, l2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], l2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, l2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], l2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f})', linewidth=2)

    ax.set_title("Liquidez Corrente das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Liquidez Corrente")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_composicao_endividamento_imobiliario():
    dados = {
        'Empresa': ['ALIANS', 'CCR', 'CYRELA', 'EZTEC', 'IGUATEMI', 'MULTIPLAN'],
        '2022': [23.04, 27.80, 41.78, 47.82, 43.34, 30.16],
        '2023': [17.02, 20.41, 38.94, 34.29, 24.97, 30.44],
        '2024': [17.22, 13.60, 32.79, 24.15, 24.87, 22.49],
        'Média': [19.76, 20.60, 37.84, 35.42, 31.06, 27.70]
    }
    df = pd.DataFrame(dados)
    media_global = 28.06

    empresas = df['Empresa']
    c2022, c2023, c2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], c2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, c2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], c2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global:.2f}%)', linewidth=2)

    ax.set_title("Composição do Endividamento das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Composição (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)


def plot_margem_liquida_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [46.53, 55.39, 5.24, 22.38, 11.88],
        '2023': [44.60, 40.70, 10.83, 31.90, 15.65],
        '2024': [42.74, 45.56, 12.36, 38.35, 17.88],
        'Média': [44.62, 46.43, 9.48, 30.88, 15.14]
    }
    df = pd.DataFrame(dados)
    media_global = 29.71

    empresas = df['Empresa']
    m2022 = df['2022']
    m2023 = df['2023']
    m2024 = df['2024']
    media = df['Média']

    fig, ax = plt.subplots(figsize=(12, 6))
    width = 0.25
    x = range(len(empresas))

    ax.bar([p - width for p in x], m2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, m2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], m2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)

    ax.axhline(media_global, color='#ff4500', linestyle='--', label='Média Global (29,71%)', linewidth=2)

    ax.set_title("Margem Líquida das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Margem Líquida (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')

    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_grau_endividamento_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [50.46, 62.61, 57.49, 77.90, 59.41],
        '2023': [53.65, 66.27, 56.66, 76.75, 55.17],
        '2024': [50.24, 66.03, 55.32, 75.49, 54.15],
        'Média': [51.45, 64.97, 56.49, 76.71, 56.24]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    e2022, e2023, e2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], e2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, e2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], e2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global}%)', linewidth=2)

    ax.set_title("Grau de Endividamento das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Endividamento (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_roe_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [16.26, 22.59, 5.44, 31.57, 18.80],
        '2023': [17.70, 20.97, 9.62, 34.93, 23.39],
        '2024': [11.50, 24.41, 10.92, 35.04, 26.00],
        'Média': [15.15, 22.66, 8.66, 33.85, 22.73]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    r2022, r2023, r2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], r2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, r2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], r2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global}%)', linewidth=2)

    ax.set_title("ROE das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("ROE (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_pl_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [5.8, 6.9, 17.0, 10.2, 4.3],
        '2023': [4.8, 8.8, 12.3, 10.1, 3.3],
        '2024': [8.69, 6.7, 9.3, 6.7, 4.9],
        'Média': [6.43, 7.47, 12.87, 9.00, 4.17]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    p2022, p2023, p2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], p2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, p2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], p2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhlin

def plot_pvpa_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [0.88, 1.57, 0.93, 3.21, 0.81],
        '2023': [0.95, 1.84, 1.18, 3.54, 0.78],
        '2024': [0.85, 1.64, 1.02, 2.36, 1.28],
        'Média': [0.89, 1.68, 1.04, 3.04, 0.96]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    v2022, v2023, v2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], v2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, v2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], v2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global})', linewidth=2)

    ax.set_title("P/VPA das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("P/VPA")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_ebitda_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [64.54, 94.26, 18.92, 57.03, 19.33],
        '2023': [63.83, 69.97, 23.64, 67.78, 23.08],
        '2024': [64.88, 77.68, 24.41, 78.03, 28.26],
        'Média': [64.42, 80.64, 22.32, 67.61, 23.56]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    e2022, e2023, e2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], e2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, e2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], e2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global})', linewidth=2)

    ax.set_title("EBITDA das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("EBITDA")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_dividend_yield_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [4.83, 15.18, 12.29, 9.01, 12.67],
        '2023': [8.59, 10.05, 3.63, 7.59, 16.27],
        '2024': [9.08, 9.63, 4.79, 7.88, 14.66],
        'Média': [7.5, 11.62, 6.90, 8.16, 14.53]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    d2022, d2023, d2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], d2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, d2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], d2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global}%)', linewidth=2)

    ax.set_title("Dividend Yield das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Dividend Yield (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_liquidez_corrente_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [2.45, 3.06, 1.3, 1.25, 1.2],
        '2023': [2.46, 2.01, 1.47, 1.46, 0.91],
        '2024': [2.98, 1.23, 1.26, 0.99, 0.86],
        'Média': [2.63, 2.10, 1.34, 1.23, 0.99]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    l2022, l2023, l2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], l2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, l2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], l2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global})', linewidth=2)

    ax.set_title("Liquidez Corrente das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Liquidez Corrente")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)

def plot_composicao_endividamento_energia():
    dados = {
        'Empresa': ['CTEEP', 'TAESA', 'COPEL', 'ENGIE', 'CEMIG'],
        '2022': [8.23, 9.51, 25.05, 19.80, 35.14],
        '2023': [13.49, 13.76, 29.43, 18.86, 43.15],
        '2024': [14.05, 18.25, 32.58, 19.22, 43.74],
        'Média': [11.92, 13.84, 29.02, 19.29, 40.68]
    }
    df = pd.DataFrame(dados)
    media_global = round(df['Média'].mean(), 2)

    empresas = df['Empresa']
    c2022, c2023, c2024, media = df['2022'], df['2023'], df['2024'], df['Média']
    x = range(len(empresas))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([p - width for p in x], c2022, width, label='2022', color='#66b3ff', edgecolor='black')
    ax.bar(x, c2023, width, label='2023', color='#ffcc99', edgecolor='black')
    ax.bar([p + width for p in x], c2024, width, label='2024', color='#99cc99', edgecolor='black')

    ax.plot(x, media, label='Média das Empresas', color='#ff6347', marker='o', linewidth=3)
    ax.axhline(media_global, color='#ff4500', linestyle='--', label=f'Média Global ({media_global}%)', linewidth=2)

    ax.set_title("Composição do Endividamento das Empresas (2022-2024)")
    ax.set_xlabel("Empresas")
    ax.set_ylabel("Composição (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(empresas, rotation=45, ha='right')
    ax.legend(loc='upper left')
    st.pyplot(fig)


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

st.title("📊 Carteira Teórica da Sala de Ações 2025")
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

# exibição das abas
aba0, aba1, aba2, aba3, aba4 = st.tabs([
    "📘 Introdução", "🏗️ Indicadores", "🏆 Ranking Final",
    "📈 Gráfico", "📊 Análise dos Indicadores"
])

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
    st.subheader("📊 Análise dos Indicadores")

    # Texto explicativo fixo
    st.markdown("""
    Esta seção analisa as principais variações dos indicadores contábeis, correlacionando-as com as justificativas apresentadas nos relatórios administrativos de cada empresa.  
    O objetivo é identificar os fatores-chave — como estratégias operacionais, cenários macroeconômicos ou eventos extraordinários — que impactaram os resultados financeiros no período avaliado.
    """)

    # Botões por setor
    if setor == "Imobiliário":
        st.markdown("#### Indicadores do Setor Imobiliário")

        if st.button("📉 Margem Líquida"):
            plot_margem_liquida_imobiliario()
        if st.button("💳 Grau de Endividamento"):
            plot_grau_endividamento_imobiliario()
        if st.button("📈 ROE"):
            plot_roe_imobiliario()
        if st.button("💵 P/L"):
            plot_pl_imobiliario()
        if st.button("🏷️ P/VPA"):
            plot_pvpa_imobiliario()
        if st.button("⚙️ EBITDA"):
            plot_ebitda_imobiliario()
        if st.button("💰 Dividend Yield"):
            plot_dividend_yield_imobiliario()
        if st.button("💧 Liquidez Corrente"):
            plot_liquidez_corrente_imobiliario()
        if st.button("🏦 Composição do Endividamento"):
            plot_composicao_endividamento_imobiliario()

    elif setor == "Energia":
        st.markdown("#### Indicadores do Setor de Energia")

        if st.button("📉 Margem Líquida"):
            plot_margem_liquida_energia()
        if st.button("💳 Grau de Endividamento"):
            plot_grau_endividamento_energia()
        if st.button("📈 ROE"):
            plot_roe_energia()
        if st.button("💵 P/L"):
            plot_pl_energia()
        if st.button("🏷️ P/VPA"):
            plot_pvpa_energia()
        if st.button("⚙️ EBITDA"):
            plot_ebitda_energia()
        if st.button("💰 Dividend Yield"):
            plot_dividend_yield_energia()
        if st.button("💧 Liquidez Corrente"):
            plot_liquidez_corrente_energia()
        if st.button("🏦 Composição do Endividamento"):
            plot_composicao_endividamento_energia()


st.markdown("---")
st.caption("Projeto de análise desenvolvido com Streamlit | Dados para uso acadêmico")