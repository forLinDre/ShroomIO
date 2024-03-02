# imports
import streamlit as st
from datetime import datetime as dt
from light import Light
from default_params import *

# light activation
sunrise = st.time_input(
    label='sunrise:',
    value=light_on_time,
    help='set your grow light on time (sunrise)',
    step=dt.timedelta(minutes=1)
)

sunset = st.time_input(
    label='sunset:',
    value=light_off_time,
    help='set your grow light off time (sunset)',
    step=dt.timedelta(minutes=1)
)

# display GUI
st.write(sunrise)
st.write(sunset)
