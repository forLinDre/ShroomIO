# imports
from gpiozero import PWMOutputDevice


class PWM(PWMOutputDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)