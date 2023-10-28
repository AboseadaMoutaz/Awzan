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

reset = st.button("New Game", type="primary")


if reset:
    game.reset(int(min), int(max))
st.text(game.get_reset_info())

st.dataframe(pd.DataFrame(data={'weight': [':red[pihiuh]']}))