import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.caption('Edgar Iván Méndez Ovando - Proyecto Sprint 7')
st.header('Visualización de datos.')
st.subheader('Autos a la venta anunciados.')

hist_checkbox = st.checkbox('Construir histograma (Kilometraje)')
scatter_checkbox = st.checkbox('Gráfico de dispersión (Año - Kilometraje)')

if hist_checkbox:
    st.write(  # escribir un mensaje
        'Histograma - Frecuencia por kilometraje')
    # crear un histograma
    fig1 = px.histogram(car_data,
                        x='odometer',
                        labels={
                            'odometer': 'Kilometraje (millas)'
                        })
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)


if scatter_checkbox:
    st.write(  # escribir un mensaje
        'Dispersión "Año - Kilometraje"')
    # crear gráfico de dispersión
    fig2 = px.scatter(car_data,
                      x="model_year",
                      y="odometer",
                      labels={
                          'odometer': 'Kilometraje (millas)',
                          'model_year': 'Modelo (año)'
                      })
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
