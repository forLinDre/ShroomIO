# imports
import streamlit as st
import time
from default_params import *

# import raspberry pi objects
from pi_objects import *

# light activation
manual_lc = st.checkbox(
    label='manual light control',
    key=1,
    value=False
)

light_on = st.checkbox(
    label='manual light control light on',
    key=2,
    value=False
)

# sunrise = st.time_input(
#     label='sunrise:',
#     key=3,
#     value=light_on_time,
#     help='set your grow light on time (sunrise)',
#     step=dt.timedelta(minutes=1)
# )
#
# sunset = st.time_input(
#     label='sunset:',
#     key=4,
#     value=light_off_time,
#     help='set your grow light off time (sunset)',
#     step=dt.timedelta(minutes=1)
# )

# display GUI
st.write(manual_lc)
st.write(light_on)
st.write(sunrise)
st.write(sunset)

while True:
    if manual_lc:
        print('manual light control on')
    else:
        print('manual light control off')
    time.sleep(5)

# tent control
# while True:
#     time_now = dt.datetime.now()
#     # control light
#     if not manual_lc:
#         if time_now.time() > sunrise and time_now.time() < sunset:
#             if not my_light.value:
#                 my_light.on()
#         else:
#             if my_light.value:
#                 my_light.off()
#     else:
#         if light_on:
#             if not my_light.value:
#                 my_light.on()
#         else:
#             if my_light.value:
#                 my_light.off()

