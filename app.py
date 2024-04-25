import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
    
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Encabezado y subtítulo
st.header('Proyecto Sprint 5')
st.write('Análisis de datos de vehículos. Selecciona el tipo de visualización')

#Casillas de verificacioón
hist_checkbox = st.checkbox('Histograma para el conjunto de datos de anuncios de venta de coches', key= 'hist_checkbox')
scatter_checkbox = st.checkbox('Diagrama de dispersión precio vs. millaje', key= 'scatter_checkbox')

#Verificar casilla seleccionada
if hist_checkbox:
    fig= px.histogram(car_data, x= 'odometer', title= 'Histograma para el conjunto de datos de venta de coches')
    #Gráfico 
    st.plotly_chart(fig, use_container_width= True)
    #Mensaje
    st.write('Datos estadísticos descriptivos')
    #Mostrar media, mediana y desviación estándar
    st.write(f"Media: {car_data['odometer'].mean():,.0f},"
             f"Mediana: {car_data['odometer'].median():,.0f},"
             f"Desviación estándar: {car_data['odometer'].std():,.0f}")
    
    if scatter_checkbox:
        #Gráico
        fig2 = px.scatter(car_data, x= 'odometer', y= 'price', title= 'Diagrama de dispersión precio vs millaje')
        st.plotly_chart(fig2, use_container_width= True)
        #Mensaje
        st.write('Relación precio-millaje')
        #Datos
        correlation = car_data['odometer'].corr(car_data['price'])
        st.write(f"Coeficiente de correlación: {correlation: .3f}")
    