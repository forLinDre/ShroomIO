# imports
import streamlit as st
import time
from default_params import *

# import raspberry pi objects
from pi_objects import *

# light activation
manual_lc = st.toggle(
    label='manual light control',
    key='manual_lc',
    value=False
)

if st.session_state.manual_lc:
    light_on = st.toggle(
        label='manual light control light on',
        key='light_on',
        value=False
    )
else:
    light_on = False
    st.session_state['light_on'] = False

sunrise = st.time_input(
    label='sunrise:',
    key='sunrise',
    value=light_on_time,
    help='set your grow light on time (sunrise)',
    step=dt.timedelta(minutes=1)
)

sunset = st.time_input(
    label='sunset:',
    key='sunset',
    value=light_off_time,
    help='set your grow light off time (sunset)',
    step=dt.timedelta(minutes=1)
)

# display GUI
st.write(manual_lc)
st.write(light_on)
st.write(sunrise)
st.write(sunset)

# tent control
while True:
    time_now = dt.datetime.now()
    # control light
    if not st.session_state.mlc:
        if time_now.time() > st.session_state.sunrise and time_now.time() < st.session_state.sunset:
            if not my_light.value:
                my_light.on()
        else:
            if my_light.value:
                my_light.off()
    else:
        if st.session_state.mlcON:
            if not my_light.value:
                my_light.on()
        else:
            if my_light.value:
                my_light.off()

    time.sleep(5)

