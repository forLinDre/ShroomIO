# imports
from pi.pwm import PWM


class Circulation(PWM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)