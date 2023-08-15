import streamlit as st
import numpy as np
import pandas as pd

st.markdown("#### Update All Data")

if st.button('Update Data'):

    bar = st.progress(0)

    loc = '../Data Sampel Final 2022/'
    saveloc = 'data/mini-data/'

    # Update Data TB
    data_kepesertaan_tb = pd.read_stata(
        loc+'Kontekstual TB/TB2021_kepesertaan.dta')

    data_kepesertaan_dm = pd.read_stata(
        loc+'Kontekstual DM/DM2021_kepesertaan.dta')

    data_kepesertaan_reg = pd.read_stata(
        loc+'Reguler/2015202101_kepesertaan.dta')

    data_kepesertaan_all = pd.concat(
        [data_kepesertaan_tb, data_kepesertaan_dm, data_kepesertaan_reg])

    bar.progress(50)

    def update_data_kepesertaan(data_kepesertaan, locbagian):

        df_prov_peta = data_kepesertaan.groupby('PSTV09').agg(
            'count').reset_index().iloc[:, 0:2]
        df_prov_peta.columns = ['PROVINSI', 'PESERTA']
        # df_prov_peta.to_stata(saveloc+locbagian+"/kepesertaan-peta.dta")
        df_prov_peta.to_csv(saveloc+locbagian +
                            "/kepesertaan-peta.csv", index=False)
        jk = data_kepesertaan.groupby('PSTV05')['PSTV05'].count()
        jk = pd.DataFrame(jk)
        jk = jk.rename_axis("jk").reset_index()
        jk.to_csv(saveloc+locbagian + "/kepesertaan-jk.csv", index=False)

    update_data_kepesertaan(data_kepesertaan_tb, "tb")
    update_data_kepesertaan(data_kepesertaan_dm, "dm")
    update_data_kepesertaan(data_kepesertaan_reg, "reguler")
    update_data_kepesertaan(data_kepesertaan_all, "all")

    bar.progress(100)

    st.write('Update Data Selesai')
