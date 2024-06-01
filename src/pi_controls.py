from light import Light
from humidifier import Humidifier

# define light control object
sun = Light(17)

# define humidifier
hum = Humidifier(
    fog_pin=27,
    fan_pin=13,
    fan_pwm_freq=25000
)
