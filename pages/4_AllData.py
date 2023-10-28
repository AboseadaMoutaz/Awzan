
import streamlit as st
import pandas as pd

from colors import Colors
from awzan_data import AwzanData

colors = Colors()

game = AwzanData()

st.set_page_config(
    page_title="Scale 2",
    page_icon="⚖️",
)

st.sidebar.success("Reveal information")

txt1 = st.text_input("pass?","")
if (txt1 == "9090"):
    choosen_info, weights, scale1_operations, scale2_operations = game.get_all_data()
    st.dataframe(choosen_info)
    st.dataframe(weights)
    st.dataframe(scale1_operations)
    st.dataframe(scale2_operations)