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
    my_light.on()
    time.sleep(1)
    my_light.off()
    time.sleep(1)
    st.write('sleeping one second')

"""
    time_now = dt.datetime.now()
    st.write(time_now)
    # control light
    if time_now.time() > sunrise and time_now.time() < sunset:
        st.write('light should be turning on')
        if not my_light.value:
            st.write('light is off but needs to be turned on')
            my_light.on()
        else:
            st.write('light is on and does not need to be turned on')
    else:
        if my_light.value:
            st.write('light is on and needs to be turned off')
            my_light.off()
        else:
            st.write('light is off and does not need to be turned on')"""