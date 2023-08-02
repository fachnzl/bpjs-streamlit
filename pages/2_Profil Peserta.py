import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_excel("shop 01.xlsx")

st.table(df)
