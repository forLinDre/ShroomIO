from light import Light
from heater import Heater
from humidifier import Humidifier
from FAE_fan import FAE
from circulation import PWM

# define light control object
sun = Light(17)

# define humidifier
hum = Humidifier(
    fog_pin=27,
    fan_pin=13,
    fan_pwm_freq=25000
)

# define heater
heat = Heater(22)

# define FAE fan
fae = FAE(5)

# define circulation fan
circ = PWM(
    pin=12,
    frequency=25000,
    active_high=True,
    initial_dc_value=0,
)
