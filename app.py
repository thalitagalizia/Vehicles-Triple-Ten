import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Dashboard de Anúncios de Carros')

hist_button = st.button('Criar histograma')
if hist_button:  #se o botão for clicado
    #escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    #criar um histograma
    # criar um histograma com os preços
    fig = px.histogram(car_data, x="price", 
                       title="Distribuição de Preços dos Veículos",
                       labels={'price': 'Preço (USD)', 'count': 'Quantidade'})
    
    #exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

 #Criar uma caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter: # só executa se a caixa estiver marcada
    st.write('Criando um gráfico de dispersão para analisar a relação entre quilometragem e preço')
    
    # Criar o gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.update_xaxes(range=[30000, 100000])
    
    # Exibir o gráfico
    st.plotly_chart(fig, use_container_width=True)