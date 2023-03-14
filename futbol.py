import pandas as pd
import plotly.express as px
import streamlit as st
import base64
import numpy as np

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('laromareda.jpg')   


st.title(':soccer: Real Zaragoza 2022-2023')
st.subheader('Toda la información de la plantilla del Real Zaragoza')
archivo_excel = 'Real_Zaragoza.xlsx'
df = pd.read_excel(archivo_excel)


st.sidebar.title('Opciones a filtrar')
st.sidebar.subheader('Filtrar por posición')
posicion = st.sidebar.selectbox('Posicion', df['Posicion'].unique())
st.sidebar.subheader('Filtrar por nacionalidad')
nacionalidad = st.sidebar.selectbox('Pais', df['Pais'].unique())
st.sidebar.subheader('Filtrar por edad')
edad = st.sidebar.slider('Edad', min_value=18, max_value=38, value=25)
st.sidebar.subheader('Filtrar por número de goles')
minutos = st.sidebar.slider('G', min_value=0, max_value=30, value=0)

st.subheader('Plantilla')
st.dataframe(df)

st.subheader('Filtrado por posición')
st.dataframe(df[df['Posicion'] == posicion])

st.subheader('Filtrado por nacionalidad')
st.dataframe(df[df['Pais'] == nacionalidad])

st.subheader('Filtrado por edad')
st.dataframe(df[df['Edad'] == edad])

st.subheader('Filtrado por número de goles')
st.dataframe(df[df['G'] == minutos])


st.subheader('Gráfico de jugadores por nacionalidad')
fig = px.histogram(df, x='Pais', color='Pais', title='Jugadores por nacionalidad')
st.plotly_chart(fig)

#crea un grafico de tarta con los jugadores que llevan TA
st.subheader('Gráfico de jugadores con % de tarjetas tarjetas amarillas del equipo')
fig = px.pie(df, values='TA', names='Nombre', title='Jugadores con tarjetas amarillas')
st.plotly_chart(fig)

#crea un grafico de area con los goles de cada jugador
st.subheader('Gráfico de jugadores con % de goles del equipo')
fig = px.area(df, x='Nombre', y='G', title='Jugadores con goles')
st.plotly_chart(fig)












































