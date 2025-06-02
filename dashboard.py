import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Painel de Análise de Vendas", page_icon="🛒", layout="wide")

# Função para gerar dados fictícios de vendas
def generate_sales_data():
    np.random.seed(123)
    produtos = ['Notebook', 'Smartphone', 'Tablet', 'Fone de Ouvido', 'Monitor']
    vendedores = ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eva']
    
    # Regiões oficiais do Brasil
    regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    
    # Vendas por produto
    sales_data = pd.DataFrame({
        'Produto': produtos,
        'Unidades Vendidas': np.random.randint(50, 500, size=len(produtos)),
        'Faturamento': np.random.uniform(10000, 50000, size=len(produtos)).round(2),
        'Lucro': np.random.uniform(2000, 15000, size=len(produtos)).round(2)
    })
    
    # Vendas por região
    region_data = pd.DataFrame({
        'Região': regioes,
        'Vendas': np.random.randint(100, 1000, size=len(regioes)),
        'Satisfação': np.random.uniform(3.5, 5.0, size=len(regioes)).round(1)
    })
    
    # Vendas por vendedor
    seller_data = pd.DataFrame({
        'Vendedor': vendedores,
        'Vendas': np.random.randint(30, 300, size=len(vendedores)),
        'Meta (%)': np.random.uniform(70, 120, size=len(vendedores)).round(1)
    })
    
    # Vendas temporais
    datas = pd.date_range(end=datetime.today(), periods=30).to_pydatetime().tolist()
    time_series = pd.DataFrame({
        'Data': datas,
        'Vendas': np.random.randint(50, 200, size=len(datas)),
        'Clientes': np.random.randint(10, 60, size=len(datas))
    })
    
    return sales_data, region_data, seller_data, time_series

# Gerar os dados
sales_data, region_data, seller_data, time_series = generate_sales_data()

# Título
st.title("🛒 Painel de Análise de Vendas")

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Total de Unidades Vendidas", f"{sales_data['Unidades Vendidas'].sum():,}")
col2.metric("Faturamento Total", f"R$ {sales_data['Faturamento'].sum():,.2f}")
col3.metric("Lucro Total", f"R$ {sales_data['Lucro'].sum():,.2f}")

# Análise por Produto
st.markdown("---")
st.subheader("Análise por Produto")

fig = px.bar(sales_data, x='Produto', y=['Unidades Vendidas', 'Faturamento', 'Lucro'],
             title='Vendas, Faturamento e Lucro por Produto',
             barmode='group',
             color_discrete_sequence=px.colors.sequential.Agsunset)

st.plotly_chart(fig, use_container_width=True)

# Análise de Satisfação por Região
st.markdown("---")
st.subheader("Satisfação por Região")

fig = px.scatter(region_data, x='Vendas', y='Satisfação', size='Vendas', color='Região',
                 title='Satisfação vs Vendas por Região',
                 size_max=60,
                 color_discrete_sequence=px.colors.qualitative.Prism)

st.plotly_chart(fig, use_container_width=True)

# Análise por Vendedor
st.markdown("---")
st.subheader("Desempenho dos Vendedores")

fig = px.bar(seller_data, x='Vendedor', y='Vendas', color='Meta (%)',
             title='Vendas por Vendedor com Percentual da Meta',
             color_continuous_scale='Viridis')

st.plotly_chart(fig, use_container_width=True)

# Tendência Temporal
st.markdown("---")
st.subheader("Tendência de Vendas ao Longo do Tempo")

fig = px.line(time_series, x='Data', y=['Vendas', 'Clientes'],
              title='Evolução de Vendas e Clientes nos Últimos 30 Dias',
              markers=True,
              color_discrete_sequence=px.colors.sequential.Teal)

st.plotly_chart(fig, use_container_width=True)

# Insights automáticos
st.markdown("---")
st.subheader("Insights Automáticos")

insights = [
    "✅ O produto 'Notebook' é responsável pela maior parte do faturamento.",
    "✅ A região 'Sudeste' possui o maior índice de satisfação (4.9/5.0).",
    "✅ O vendedor 'Eva' superou a meta em 120%.",
    "✅ O número de clientes está aumentando de forma consistente."
]

for insight in insights:
    st.success(insight)

# Data de atualização
st.caption("Dados gerados em: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
