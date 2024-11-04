import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)

#criar o cache
@st.cache_data
def  load_data():
    # Carregar o arquivo CSV
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    df.set_index("Track", inplace=True)
    return df

# Armazenar o df original no session_state
df = load_data()
st.session_state["df_spotify"] = df

# Gera coordenadas únicas de latitude e longitude dentro dos limites do Brasil para cada música
np.random.seed(42)  # Define uma seed para resultados reproduzíveis
df["latitude"] = np.random.uniform(-34.0, 5.0, size=len(df))    # Limites de latitude do Brasil
df["longitude"] = np.random.uniform(-74.0, -34.0, size=len(df))  # Limites de longitude do Brasil

# Seleção de artista no sidebar
artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

# Seleção de álbum com base no artista selecionado
albuns = df_filtered['Album'].value_counts().index
album = st.sidebar.selectbox("Album", albuns)
df_filtered_2 = df[df["Album"] == album]

# Criação das colunas para gráficos
col1, col2 = st.columns([0.7, 0.3])

# Gráfico de barras para "Stream" usando Plotly em azul turquesa
with col1:
    fig_stream = px.bar(
        df_filtered_2,
        x=df_filtered_2.index,
        y="Stream",
        title="Stream",
        labels={"x": "Tracks", "Stream": "Streams"},
        color_discrete_sequence=["turquoise"]
    )
    st.plotly_chart(fig_stream)

# Gráfico de barras para "Danceability" usando Plotly em azul turquesa
with col2:
    fig_danceability = px.bar(
        df_filtered_2,
        x=df_filtered_2.index,
        y="Danceability",
        title="Danceability",
        labels={"x": "Tracks", "Danceability": "Danceability Score"},
        color_discrete_sequence=["pink"]
    )
    st.plotly_chart(fig_danceability)

# Exibir o DataFrame filtrado
st.dataframe(df_filtered_2)

# Gráfico de mapa usando as colunas de latitude e longitude únicas para cada música no Brasil
st.write("Mapa de Localização das Músicas no Brasil")

fig_map = px.scatter_mapbox(
    df_filtered_2,
    lat="latitude",
    lon="longitude",
    size="Stream",  # Tamanho dos pontos baseado na quantidade de streams
    color="Danceability",  # Cor dos pontos baseada na danceability
    hover_name=df_filtered_2.index,  # Nome das músicas ao passar o mouse
    zoom=3,  # Nível de zoom do mapa
    title="Mapa de Localização das Músicas no Brasil"
)

# Configuração do estilo do mapa
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Exibe o gráfico de mapa
st.plotly_chart(fig_map)
