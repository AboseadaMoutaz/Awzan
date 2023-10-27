import streamlit as st
import pandas as pd

from colors import Colors
from awzan_data import AwzanData

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

left_total_1 = game.get_scale_hand_total_count(0, True)
right_total_1 = game.get_scale_hand_total_count(0, False)

st.text("Important scale :\n")
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

scal1_add1, scal1_add2 = st.columns(2)
with scal1_add1:
    scale1_add_count1_l = st.slider(str(colors.colors[0]) + ' Left 1', 0, 4, 0)
    scale1_add_count2_l = st.slider(str(colors.colors[1]) + ' Left 1', 0, 4, 0)
    scale1_add_count3_l = st.slider(str(colors.colors[2]) + ' Left 1', 0, 4, 0)
    scale1_add_count4_l = st.slider(str(colors.colors[3]) + ' Left 1', 0, 4, 0)
    scale1_add_count5_l = st.slider(str(colors.colors[4]) + ' Left 1', 0, 4, 0)
with scal1_add2:
    scale1_add_count1_r = st.slider(str(colors.colors[0]) + ' Right 1', 0, 4, 0)
    scale1_add_count2_r = st.slider(str(colors.colors[1]) + ' Right 1', 0, 4, 0)
    scale1_add_count3_r = st.slider(str(colors.colors[2]) + ' Right 1', 0, 4, 0)
    scale1_add_count4_r = st.slider(str(colors.colors[3]) + ' Right 1', 0, 4, 0)
    scale1_add_count5_r = st.slider(str(colors.colors[4]) + ' Right 1', 0, 4, 0)
add_scale1 = st.button("Add Scale 1", type="primary")


if add_scale1:
    game.add_scale_weight(0,[scale1_add_count1_l, scale1_add_count2_l, scale1_add_count3_l, scale1_add_count4_l, scale1_add_count5_l]
                          ,[scale1_add_count1_r, scale1_add_count2_r, scale1_add_count3_r, scale1_add_count4_r, scale1_add_count5_r])
    st.text("Important scale updated :\n")
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

if left_total_1 == right_total_1:
    st.divider()
    st.text("Congrats on equal balance, wanna check weights?")
    w1 = st.slider(str(colors.colors[0]) + ' wight?', int(min), int(max), 0)
    w2 = st.slider(str(colors.colors[1]) + ' wight?', int(min), int(max), 0)
    w3 = st.slider(str(colors.colors[2]) + ' wight?', int(min), int(max), 0)
    w4 = st.slider(str(colors.colors[3]) + ' wight?', int(min), int(max), 0)
    w5 = st.slider(str(colors.colors[4]) + ' wight?', int(min), int(max), 0)
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

st.divider()
st.divider()
st.text("Not Important scale :\n")
scale2_col1, scale2_col2, scale2_col3, scale2_col4, scale2_col5 = st.columns(5)
with scale2_col1:
    st.markdown(colors.get_text(game.get_scale_hand_count(1,True)))
with scale2_col2:
    st.text(" | ")
with scale2_col3:
    left_total_2 = game.get_scale_hand_total_count(1, True)
    right_total_2 = game.get_scale_hand_total_count(1, False)
    text = ""
    if left_total_2 == right_total_2:
        text = " = "
    elif left_total_2 > right_total_2:
        text = " > "
    elif left_total_2 < right_total_2:
        text = " < "
    st.text(text)
with scale2_col4:
    st.text(" | ")
with scale2_col5:
    st.markdown(colors.get_text(game.get_scale_hand_count(1,False)))

scal1_add1, scal1_add2 = st.columns(2)
with scal1_add1:
    scale2_add_count1_l = st.slider(str(colors.colors[0]) + ' Left 2', 0, 4, 0)
    scale2_add_count2_l = st.slider(str(colors.colors[1]) + ' Left 2', 0, 4, 0)
    scale2_add_count3_l = st.slider(str(colors.colors[2]) + ' Left 2', 0, 4, 0)
    scale2_add_count4_l = st.slider(str(colors.colors[3]) + ' Left 2', 0, 4, 0)
    scale2_add_count5_l = st.slider(str(colors.colors[4]) + ' Left 2', 0, 4, 0)
with scal1_add2:
    scale2_add_count1_r = st.slider(str(colors.colors[0]) + ' Right 2', 0, 4, 0)
    scale2_add_count2_r = st.slider(str(colors.colors[1]) + ' Right 2', 0, 4, 0)
    scale2_add_count3_r = st.slider(str(colors.colors[2]) + ' Right 2', 0, 4, 0)
    scale2_add_count4_r = st.slider(str(colors.colors[3]) + ' Right 2', 0, 4, 0)
    scale2_add_count5_r = st.slider(str(colors.colors[4]) + ' Right 2', 0, 4, 0)
add_scale2 = st.button("Add Scale 2", type="primary")

if add_scale2:
    game.add_scale_weight(1,[scale2_add_count1_l, scale2_add_count2_l, scale2_add_count3_l, scale2_add_count4_l, scale2_add_count5_l]
                          ,[scale2_add_count1_r, scale2_add_count2_r, scale2_add_count3_r, scale2_add_count4_r, scale2_add_count5_r])
    st.text("Not Important scale updated :\n")
    scale2_col1, scale2_col2, scale2_col3, scale2_col4, scale2_col5 = st.columns(5)
    with scale2_col1:
        st.markdown(colors.get_text(game.get_scale_hand_count(1,True)))
    with scale2_col2:
        st.text(" | ")
    with scale2_col3:
        left_total_2 = game.get_scale_hand_total_count(1, True)
        right_total_2 = game.get_scale_hand_total_count(1, False)
        text = ""
        if left_total_2 == right_total_2:
            text = " = "
        elif left_total_2 > right_total_2:
            text = " > "
        elif left_total_2 < right_total_2:
            text = " < "
        st.text(text)
    with scale2_col4:
        st.text(" | ")
    with scale2_col5:
        st.markdown(colors.get_text(game.get_scale_hand_count(1,False)))



