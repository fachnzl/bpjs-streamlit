import streamlit as st
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import json
import requests
import geopandas as gpd
from datetime import datetime, date

import folium
from folium.plugins import FastMarkerCluster
from branca.colormap import LinearColormap
from folium.features import GeoJsonPopup, GeoJsonTooltip
from streamlit_folium import folium_static

st.set_page_config(layout="wide")
with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)


# opt = st.sidebar.radio("Select Any Graph", options=("Line", "Bar", "H-Bar"))

# st.markdown("## Main Dashboard")

if 'kategori' not in st.session_state:
    st.session_state['kategori'] = 'All'
    kat = 0
else:
    if st.session_state['kategori'] == "All":
        kat = 0
    elif st.session_state['kategori'] == "Tuberkulosis":
        kat = 1
    elif st.session_state['kategori'] == "Diabetes Mellitus":
        kat = 2
    elif st.session_state['kategori'] == "Reguler":
        kat = 3

rad = st.radio(
    "kategori",
    ["All", "Tuberkulosis", "Diabetes Mellitus", "Reguler"],
    index=kat,
    key="visibility",
    # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        horizontal=True,
)
st.session_state['kategori'] = rad

# Read Data
loc = 'data/'
# tb2021_kepesertaan = pd.read_stata(loc+'Kontekstual TB/TB2021_kepesertaan.dta')
# dm2021_kepesertaan = pd.read_stata(loc+'Kontekstual DM/DM2021_kepesertaan.dta')
# reguler_kepesertaan = pd.read_stata(loc+'Reguler/2015202101_kepesertaan.dta')
# kepesertaan_all = pd.concat(
#     [tb2021_kepesertaan, dm2021_kepesertaan, reguler_kepesertaan])
# End of read data
if st.session_state['kategori'] == "All":
    # tb2021_kepesertaan = pd.read_stata(
    #     loc+'Kontekstual TB/TB2021_kepesertaan.dta')
    # dm2021_kepesertaan = pd.read_stata(
    #     loc+'Kontekstual DM/DM2021_kepesertaan.dta')
    # reguler_kepesertaan = pd.read_stata(
    #     loc+'Reguler/2015202101_kepesertaan.dta')
    # data_kepesertaan = pd.concat(
    #     [tb2021_kepesertaan, dm2021_kepesertaan, reguler_kepesertaan])
    data_loc = 'mini-data/all/'
elif st.session_state['kategori'] == "Tuberkulosis":
    # data_kepesertaan = pd.read_stata(
    #     loc+'Kontekstual TB/TB2021_kepesertaan.dta')
    data_loc = 'mini-data/tb/'
elif st.session_state['kategori'] == "Diabetes Mellitus":
    # data_kepesertaan = pd.read_stata(
    #     loc+'Kontekstual DM/DM2021_kepesertaan.dta')
    data_loc = 'mini-data/dm/'
elif st.session_state['kategori'] == "Reguler":
    # data_kepesertaan = pd.read_stata(loc+'Reguler/2015202101_kepesertaan.dta')
    data_loc = 'mini-data/reguler/'
    # st.markdown(rad)

    # Fisrt Row
col1, col2, col3, col4 = st.columns(4)

col1.markdown("Jumlah Peserta BPJS 2021")
# jumlah_peserta = len(data_kepesertaan)
jumlah_peserta = 12344
col1.markdown('{:,}'.format(jumlah_peserta))
col1.markdown("<div class='green-box'></div>", unsafe_allow_html=True)

col2.markdown("Kunjungan Kapitasi")
col2.markdown('{:,}'.format(32432423))

col3.markdown("Kunjungan RKTL")
col3.markdown('{:,}'.format(32432423))

col4.markdown("Kunjungan Non Kapitasi")
col4.markdown('{:,}'.format(32432423))

# end of first row

# Second Row
col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("###### Sebaran Peserta BPJS")
    df_prov = pd.read_csv(loc+data_loc+"kepesertaan-peta.csv")
    # st.table(df_prov)
    # with open(loc+'shp/SHP Indonesia/geojson_prov.json', 'r') as openfile:
    #     geo_json_data = json.load(openfile)
    prov_shp = gpd.read_file(loc + "shp/SHP Indonesia/prov small/prov1.shp")
    prov_shp_merged = prov_shp.merge(df_prov, on='PROVINSI', how='left')
    geo_json_data = prov_shp_merged.to_json()

    map_ams_price = folium.Map(
        location=[-2.2333, 117.2841], zoom_start=4, tiles="cartodbpositron")
    # folium.TileLayer(opacity=0).add_to(map_ams_price)
    choropleth1 = folium.Choropleth(
        geo_data=geo_json_data,
        data=df_prov,
        columns=['PROVINSI', 'PESERTA'],
        key_on='feature.properties.PROVINSI',
        fill_color='BuGn',
        fill_opacity=1,
        line_opacity=0.2,
        legend_name='Jumlah Peserta BPJS',
        reset=True,
        highlight=False,
    ).add_to(map_ams_price)

    choropleth1.geojson.add_child(
        folium.features.GeoJsonTooltip(fields=['PROVINSI', 'PESERTA'],
                                       aliases=['PROVINSI',
                                                'PESERTA BPJS'],
                                       labels=True,
                                       localize=True,
                                       sticky=False,
                                       style="""
                                    background-color: #F0EFEF;
                                    border: 0px solid black;
                                    border-radius: 3px;
                                    box-shadow: 3px;
                                    """,)
    )

    # folium_static(map_ams_price, width=610, height=250)
    folium_static(map_ams_price)

with col2:
    col2.markdown("###### Persentase Peserta BPJS menurut Jenis Kelamin")
    # jk = data_kepesertaan.groupby('PSTV05')['PSTV05'].count()
    # jk = pd.DataFrame(jk)
    # jk = jk.rename_axis("jk").reset_index()
    jk = pd.read_csv(loc+data_loc+"kepesertaan-jk.csv")
    fig = go.Figure(
        data=[go.Pie(labels=jk['jk'], values=jk['PSTV05'], hole=.6)])
    fig.update_traces(marker=dict(colors=["#05A04A", "#0B796E"]))
    fig.update_layout(height=200, legend=dict(
        yanchor="top", y=0.001, xanchor="left", x=0.01), margin=dict(t=0, b=0, l=0, r=0))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'
    })
    st.plotly_chart(fig, use_container_width=True)
