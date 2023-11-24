import streamlit as st
import random as rand


st.write('Yellow')


if st.button('Make it rain'):
    if rand.random() > 0.5:
        st.balloons()
    else:
        st.snow()
