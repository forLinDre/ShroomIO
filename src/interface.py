# imports
import pandas as pd
import streamlit as st
import time
from default_params import *
from environment import Environment

# import raspberry pi objects
from pi_objects import *
# import random
# 
# class TempLight:
#     def __init__(self):
#         pass
# 
#     def on(self):
#         pass
# 
#     def off(self):
#         pass
# 
#     @property
#     def value(self):
#         return random.choice([0, 1])
# 
# 
# sun = TempLight()

# light interface
light_expander = st.sidebar.expander('Light Control :sun_with_face:')

manual_lc = light_expander.toggle(
    label='manual light control',
    key='manual_lc',
    value=False
)

ml_on = light_expander.toggle(
    label='light',
    key='ml_on',
    value=False,
    disabled=False if st.session_state.manual_lc else True
)

sunrise = light_expander.time_input(
    label='sunrise:',
    key='sunrise',
    value=def_light_on_time,
    help='set your grow light on time (sunrise)',
    step=dt.timedelta(minutes=5)
)

sunset = light_expander.time_input(
    label='sunset:',
    key='sunset',
    value=def_light_off_time,
    help='set your grow light off time (sunset)',
    step=dt.timedelta(minutes=5)
)

# humidity interface
hum_expander = st.sidebar.expander('Humidity Control :sweat_drops:')

hum_control = hum_expander.toggle(
    label='Humidity Control',
    key='hum_control',
    value=True
)

hum_set = hum_expander.slider(
    label='Humidity Setting (R.H.)',
    key='hum_set',
    min_value=50,
    max_value=100,
    value=def_hum,
    step=1,
    disabled=False if st.session_state.hum_control else True
)

hum_tol = hum_expander.number_input(
    label='On/Off Tolerance',
    key='hum_tol',
    min_value=1,
    max_value=15,
    value=def_hum_tol,
    step=1,
    disabled=False if st.session_state.hum_control else True
)

hum_fan = hum_expander.slider(
    label='Humidity Blower Duty Cycle',
    key='hum_fan',
    min_value=0,
    max_value=100,
    value=def_hum_dc,
    disabled=False if st.session_state.hum_control else True
)


# temperature interface
temp_expander = st.sidebar.expander('Temperature Control :thermometer:')

temp_control = temp_expander.toggle(
    label='Temperature Control',
    key='temp_control',
    value=True
)

temp_set = temp_expander.slider(
    label='Temperature Setting (deg. F)',
    key='temp_set',
    min_value=50,
    max_value=90,
    value=def_temp,
    step=1,
    disabled=False if st.session_state.temp_control else True
)

temp_tol = temp_expander.number_input(
    label='On/Off Tolerance',
    key='temp_tol',
    min_value=1,
    max_value=15,
    value=def_temp_tol,
    step=1,
    disabled=False if st.session_state.temp_control else True
)

# FAE interface
fae_expander = st.sidebar.expander('FAE Control :wind_blowing_face:')

fae_control = fae_expander.toggle(
    label='Fresh Air Control',
    key='fae_control',
    value=True
)

co2_set = fae_expander.slider(
    label='CO2 Setting (PPM)',
    key='co2_set',
    min_value=50,
    max_value=1500,
    value=def_max_co2_ppm,
    step=50,
    disabled=False if st.session_state.fae_control else True
)

co2_tol = fae_expander.number_input(
    label='On/Off Tolerance',
    key='co2_tol',
    min_value=10,
    max_value=100,
    value=def_co2_tol,
    step=10,
    disabled=False if st.session_state.fae_control else True
)

# air circulation interface
air_expander = st.sidebar.expander('Air Circulation Control :tornado:')

air_circ = air_expander.toggle(
    label='Air Circulation',
    key='air_circ',
    value=True
)

circ_fan = air_expander.slider(
    label='Air Circulation Fan Duty Cycle',
    key='circ_fan',
    min_value=5,
    max_value=100,
    value=def_circ_dc,
    step=5,
    disabled=False if st.session_state.air_circ else True
)

if 'env' not in st.session_state:
    env = Environment.start_capture()
    st.session_state['env'] = env
    chart_pl = st.empty()
    my_chart = chart_pl.line_chart(env.data)
    # st.session_state['my_chart'] = my_chart
else:
    env = st.session_state['env']
    chart_pl = st.empty()
    my_chart = chart_pl.line_chart(env.data)
    # my_chart = st.session_state['my_chart']
    # chart_pl.write(my_chart)


# tent control
while True:
    time_now = dt.datetime.now()

    # light control
    if not st.session_state.manual_lc:
        if time_now.time() > st.session_state.sunrise and time_now.time() < st.session_state.sunset:
            if not sun.value:
                sun.on()
        else:
            if sun.value:
                sun.off()
    else:
        if st.session_state.ml_on:
            if not sun.value:
                sun.on()
        else:
            if sun.value:
                sun.off()

    num_rows = env.data.shape[0]
    if num_rows == env.init_rows:
        chart_pl.empty()
        env.get_sample()
        chart_pl.line_chart(env.data)
    else:
        env.get_sample()
        my_chart.add_rows(env.data.iloc[-1])

    st.session_state['env'] = env
    # st.session_state['my_chart'] = my_chart

    time.sleep(pd.Timedelta(run_freq).total_seconds())

