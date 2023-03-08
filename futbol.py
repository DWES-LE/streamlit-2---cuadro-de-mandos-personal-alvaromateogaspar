import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Bundesliga 2016/2017")


url = "https://raw.githubusercontent.com/footballcsv/deutschland/master/2010s/2016-17/de.1.csv"

df = pd.read_csv(url)

st.write('Consultar jornadas')

# Crear una lista de las jornadas únicas
jornadas = df["Matchday"].unique().tolist()

# Crear el menú desplegable de las jornadas
jornada_seleccionada = st.selectbox("Selecciona una jornada", jornadas)

# Filtrar el DataFrame original para mostrar solo los datos de la jornada seleccionada
df_filtrado = df.loc[df["Matchday"] == jornada_seleccionada]

# Mostrar los datos filtrados en una tabla
st.dataframe(df_filtrado)

st.write('Consultar partidos locales de un equipo')

# Crear una lista para consultar los partidos locales de un equipo

# Crear el menú desplegable de los equipos
equipo_seleccionado = st.selectbox(
    "Selecciona un equipo", df["Team 1"].unique().tolist())

# Filtrar el DataFrame original para mostrar solo los datos de los partidos locales del equipo seleccionado
df_filtrado = df.loc[df["Team 1"] == equipo_seleccionado]

# Mostrar los datos filtrados en una tabla
st.dataframe(df_filtrado)

st.write('Consultar partidos visitantes de un equipo')


# Crear una lista para consultar los partidos visitantes de un equipo

# Crear el menú desplegable de los equipos
equipo_seleccionado = st.selectbox(
    "Selecciona un equipo", df["Team 2"].unique().tolist())

# Filtrar el DataFrame original para mostrar solo los datos de los partidos visitantes del equipo seleccionado
df_filtrado = df.loc[df["Team 2"] == equipo_seleccionado]

# Mostrar los datos filtrados en una tabla
st.dataframe(df_filtrado)

#filtrar partidos por fecha

st.write('Consultar partidos por fecha')

# Crear una lista para consultar los partidos por fecha

# Crear el menú desplegable de los equipos
fecha_seleccionada = st.selectbox(
    "Selecciona una fecha", df["Date"].unique().tolist())

# Filtrar el DataFrame original para mostrar solo los datos de los partidos visitantes del equipo seleccionado
df_filtrado = df.loc[df["Date"] == fecha_seleccionada]

# Mostrar los datos filtrados en una tabla
st.dataframe(df_filtrado)





























