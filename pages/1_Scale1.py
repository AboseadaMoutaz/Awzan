import streamlit as st
import pandas as pd

from colors import Colors
from awzan_data import AwzanData

colors = Colors()

game = AwzanData()

st.set_page_config(
    page_title="Scale 1",
    page_icon="⚖️",
)

st.sidebar.success("Important Scale information")

min, max = game.get_min_max()

st.header("Important scale")
scale1_col1, scale1_col2, scale1_col3, scale1_col4, scale1_col5 = st.columns(5)
with scale1_col1:
    st.markdown(colors.get_text(game.get_scale_hand_count(0,True)))
with scale1_col2:
    st.text(" | ")
with scale1_col3:
    left_total_1 = game.get_scale_hand_total_count(0, True)
    right_total_1 = game.get_scale_hand_total_count(0, False)
    text = ""
    if left_total_1 == right_total_1:
        text = " = "
    elif left_total_1 > right_total_1:
        text = " > "
    elif left_total_1 < right_total_1:
        text = " < "
    st.text(text)
with scale1_col4:
    st.text(" | ")
with scale1_col5:
    st.markdown(colors.get_text(game.get_scale_hand_count(0,False)))

left_string = '[Left]'
right_string = '[Right]'
scal1_add1, scal1_add2 = st.columns(2)
with scal1_add1:
    scale1_add_count1_l = st.slider(':' + str(colors.colors[0]) + left_string, 0, 4, 0)
    scale1_add_count2_l = st.slider(':' + str(colors.colors[1]) + left_string, 0, 4, 0)
    scale1_add_count3_l = st.slider(':' + str(colors.colors[2]) + left_string, 0, 4, 0)
    scale1_add_count4_l = st.slider(':' + str(colors.colors[3]) + left_string, 0, 4, 0)
    scale1_add_count5_l = st.slider(':' + str(colors.colors[4]) + left_string, 0, 4, 0)
with scal1_add2:
    scale1_add_count1_r = st.slider(':' + str(colors.colors[0]) + right_string, 0, 4, 0)
    scale1_add_count2_r = st.slider(':' + str(colors.colors[1]) + right_string, 0, 4, 0)
    scale1_add_count3_r = st.slider(':' + str(colors.colors[2]) + right_string, 0, 4, 0)
    scale1_add_count4_r = st.slider(':' + str(colors.colors[3]) + right_string, 0, 4, 0)
    scale1_add_count5_r = st.slider(':' + str(colors.colors[4]) + right_string, 0, 4, 0)
add_scale1 = st.button("Add to Scale", type="primary")


st.markdown(game.get_all_logs(0))
