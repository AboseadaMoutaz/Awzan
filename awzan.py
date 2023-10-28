import streamlit as st
import pandas as pd

from colors import Colors
from awzan_data import AwzanData

st.set_page_config(
    page_title="New Game",
    page_icon="⚖️",
)

st.sidebar.success("Create a new Game")
st.header('New Game')
colors = Colors()

game = AwzanData()
min, max = game.get_min_max()
min_col, max_col = st.columns(2)
with min_col:
    min = st.text_input("Minimum Weight = ", str(min))
with max_col:
    max = st.text_input("Minimum Weight = ", str(max))

new_game_pass = st.text_input('New Game password','')
reset = st.button("New Game", type="primary")


if reset== True and new_game_pass == '701':
    game.reset(int(min), int(max))
st.text(game.get_reset_info())
