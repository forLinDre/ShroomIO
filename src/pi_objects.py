from light import Light
from pi.co2_sensor import MHZ19

# define light control object
sun = Light(17)

# define humidity sensor
co2 = MHZ19()

# define co2 sensor