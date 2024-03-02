# imports
from gpiozero import DigitalOutputDevice


class Light(DigitalOutputDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


