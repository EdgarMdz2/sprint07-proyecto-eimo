import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto Sprint-07')
hist_checkbox = st.checkbox('Construir histograma')
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

if hist_checkbox:
    st.write(  # escribir un mensaje
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig1 = px.histogram(car_data, x='odometer')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)


if scatter_checkbox:
    st.write(  # escribir un mensaje
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
