# imports
from src.pi.on_off_relay import OFRelay
from src.pi.pwm import PWM


class Humidity(OFRelay, PWM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)