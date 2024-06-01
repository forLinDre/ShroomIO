# imports
from gpiozero import PWMOutputDevice


class PWM(PWMOutputDevice):
    def __init__(self, pin, active_high=True, initial_dc_value=0, frequency=25000):
        PWMOutputDevice.__init__(
            self,
            pin=pin,
            active_high=active_high,
            initial_value=initial_dc_value,
            frequency=frequency
        )