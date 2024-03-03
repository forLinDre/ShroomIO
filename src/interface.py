# imports
import streamlit as st
import time
from default_params import *

# import raspberry pi objects
from pi_objects import *

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

# tent control
while True:
    time_now = dt.datetime.now()
    # control light
    if time_now.time() > sunrise and time_now.time() < sunset:
        if not my_light.value:
            my_light.on()
    else:
        if my_light.value:
            my_light.off()

    time.sleep(1)

