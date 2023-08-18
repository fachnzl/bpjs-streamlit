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

loc = 'data/'

data_loc = 'mini-data/all/'

col1 = st.columns(1)

with col1[0]:

    st.markdown("###### Sebaran Peserta BPJS")
    df_prov = pd.read_csv(loc+data_loc+"kepesertaan-peta.csv")
    # st.table(df_prov)
    # with open(loc+'shp/SHP Indonesia/geojson_prov.json', 'r') as openfile:
    #     geo_json_data = json.load(openfile)
    prov_shp = gpd.read_file(loc + "shp/SHP Indonesia/prov small/prov1.shp")
    prov_shp_merged = prov_shp.merge(df_prov, on='PROVINSI', how='left')
    geo_json_data = prov_shp_merged.to_json()

    map_ams_price = folium.Map(
        location=[-2.2333, 117.2841], zoom_start=5, tiles="OpenStreetMap")
    # folium.TileLayer(opacity=0).add_to(map_ams_price)
    # choropleth1 = folium.Choropleth(
    #     geo_data=geo_json_data,
    #     data=df_prov,
    #     columns=['PROVINSI', 'PESERTA'],
    #     key_on='feature.properties.PROVINSI',
    #     fill_color='BuGn',
    #     fill_opacity=1,
    #     line_opacity=0.2,
    #     legend_name='Jumlah Peserta BPJS',
    #     reset=True,
    #     highlight=False,
    # ).add_to(map_ams_price)

    # choropleth1.geojson.add_child(
    #     folium.features.GeoJsonTooltip(fields=['PROVINSI', 'PESERTA'],
    #                                    aliases=['PROVINSI',
    #                                             'PESERTA BPJS'],
    #                                    labels=True,
    #                                    localize=True,
    #                                    sticky=False,
    #                                    style="""
    #                                     background-color: #F0EFEF;
    #                                     border: 0px solid black;
    #                                     border-radius: 3px;
    #                                     box-shadow: 3px;
    #                                     """,)
    # )

    # folium_static(map_ams_price, width=610, height=250)
    folium_static(map_ams_price)
    st.markdown("<style>iframe{height:80vh;}</style>", unsafe_allow_html=True)
