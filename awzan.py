import streamlit as st
import pandas as pd


from scale import Scale
from wazn import Wazn
from awzan_game import AwzanGame

awzan_game = AwzanGame(1)

# Game Setup
print( "try")
reset = st.button("New Game", type="primary")


if reset:
    st.text(awzan_game.new_game())


scale1_text = awzan_game.get_scale_weights(1)
st.text_area("Scale important", scale1_text)
b1  = st.text_input("weight 1 ","( first letter)" )
is_left1 = st.checkbox('Is left weight1?')
b2  = st.text_input("weight 2 ","( first letter)" )
is_left2 = st.checkbox('Is left weight 2?')
add1 = st.button("Add to Scale important")

if add1:
    
    print(awzan_game.get_weight(b1))
    awzan_game.add_weight(1, awzan_game.get_weight(b1),is_left1 )
    awzan_game.add_weight(1, awzan_game.get_weight(b2),is_left2 )
    scale1_text = awzan_game.get_scale_weights(1)
    st.text(awzan_game.get_scale_heavy(1))





