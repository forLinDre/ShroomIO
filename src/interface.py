# imports
import streamlit as st
import time
from default_params import *

# import raspberry pi objects
from pi_objects import *

# light activation
manual_lc = st.checkbox(
    label='manual light control',
    key='mlc',
    value=False
)

light_on = st.checkbox(
    label='manual light control light on',
    key='mlcON',
    value=False
)

sunrise = st.time_input(
    label='sunrise:',
    key='sr',
    value=light_on_time,
    help='set your grow light on time (sunrise)',
    step=dt.timedelta(minutes=1)
)

sunset = st.time_input(
    label='sunset:',
    key='ss',
    value=light_off_time,
    help='set your grow light off time (sunset)',
    step=dt.timedelta(minutes=1)
)

print(st.session_state.mlc)
print(st.session_state.mlcON)

# display GUI
st.write(manual_lc)
st.write(light_on)
st.write(sunrise)
st.write(sunset)

# tent control
while True:
    time_now = dt.datetime.now()
    # control light
    if not manual_lc:
        print('manual light control off')
        if time_now.time() > sunrise and time_now.time() < sunset:
            print('at this time, light should be on')
            if not my_light.value:
                print('light currently off, turning light on')
                my_light.on()
        else:
            print('at this time, light should be off')
            if my_light.value:
                print('light currently on, turning light off')
                my_light.off()
    else:
        print('manual light control')
        if light_on:
            print('light on command')
            print(st.session_state.mlc)
            print(st.session_state.mlcON)
            if not my_light.value:
                print('light not on, turning on')
                my_light.on()
        else:
            print('light off command')
            print(st.session_state.mlc)
            print(st.session_state.mlcON)
            if my_light.value:
                print('light on, turning off')
                my_light.off()

    time.sleep(5)

