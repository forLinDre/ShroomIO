# imports
import datetime as dt

# functional parameters
run_freq = '0.1s'

# light parameters
# sunrise time
def_light_on_time = dt.time(hour=7, minute=0, second=0)
# sunset time
def_light_off_time = dt.time(hour=19, minute=0, second=0)

# humidity parameters
# default humidity target
def_hum = 90
# default on/off humidity control tolerance band
def_hum_tol = 5
# default humidity fan duty cycle
def_hum_dc = 100

# temperature parameters
# default temperature setting
def_temp = 65
# default on/off control tolerance band
def_temp_tol = 5

# FAE parameters
# max CO2 ppm
def_max_co2_ppm = 500
# default on/off control tolerance band
def_co2_tol = 50

# air circulation parameters
# default air circulation enabled
def_circ_on = True
# default air circulation fan duty cycle
def_circ_dc = 50
