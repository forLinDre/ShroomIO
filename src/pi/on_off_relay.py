# imports
from gpiozero import DigitalOutputDevice


class OFRelay(DigitalOutputDevice):
    def __init__(self, pin, active_high=True, initial_value=False):
        DigitalOutputDevice.__init__(
            self,
            pin=pin,
            active_high=active_high,
            initial_value=initial_value
        )
