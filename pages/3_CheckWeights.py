import streamlit as st
import pandas as pd

from colors import Colors
from awzan_data import AwzanData

colors = Colors()

game = AwzanData()

st.set_page_config(
    page_title="Check Weights?",
    page_icon=":scales:",
)

st.sidebar.success("Check Weights?")

st.header('Check Weights?')

min, max = game.get_min_max()

left_total_1 = game.get_scale_hand_total_count(0, True)
right_total_1 = game.get_scale_hand_total_count(0, False)

if left_total_1 == right_total_1:
    st.divider()
    st.text("Congrats on equal balance, wanna check weights?")
    w1 = st.slider(':' + str(colors.colors[0]) + '[wight?]', int(min), int(max), 0)
    w2 = st.slider(':' + str(colors.colors[1]) + '[wight?]', int(min), int(max), 0)
    w3 = st.slider(':' + str(colors.colors[2]) + '[wight?]', int(min), int(max), 0)
    w4 = st.slider(':' + str(colors.colors[3]) + '[wight?]', int(min), int(max), 0)
    w5 = st.slider(':' + str(colors.colors[4]) + '[wight?]', int(min), int(max), 0)
    check = st.button("Check weights", type="primary")
    if check:
        verified = game.verify_weights([w1,w2,w3,w4,w5])
        if verified:
            st.text( 'Congrats you won !')
            st.balloons()
            s1,s2 = game.get_scale_hand_total_dataframe()
            st.text("Scale 1")
            st.line_chart(s1)
            st.text("Scale 2")
            st.line_chart(s2)
        else:
            st.text( 'you Failed ! ;p')
else:
    st.text('Important Scale is not Balanced')