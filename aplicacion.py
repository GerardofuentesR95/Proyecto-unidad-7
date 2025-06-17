import pandas as pd
import streamlit as st
import plotly_express as px
car_data = pd.read_csv('vehicles_us.csv')
show_hist = st.checkbox('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de ventas totales de coches por modelos')
    fig = px.histogram(car_data, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: modelo vs precio')
    fig2 = px.scatter(car_data, x="model", y="price")
    st.plotly_chart(fig2, use_container_width=True)
