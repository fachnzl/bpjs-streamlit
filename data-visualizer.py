import streamlit as st
import pandas as pd

with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Data Visualizer</h1>",
            unsafe_allow_html=True)
st.markdown("---",
            unsafe_allow_html=True)

files_names = list()
files = st.file_uploader("Upload Multiple Files", type=[
                         "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        files_names.append(file.name)
    selected_files = st.multiselect("Select Files", options=files_names)
    if selected_files:
        option = st.radio("Select Entity against Date", options=[
                          "None", "GPU", "CPU", "MOUSE", "KEYBOARD", "CASING"])
        if option != "None":
            for file in files:
                if file.name in selected_files:
                    shop_data = pd.read_excel(file, index_col=0)
                    st.write(shop_data[option])
