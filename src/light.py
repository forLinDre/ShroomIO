# imports
from pi.on_off_relay import OFRelay


class Light(OFRelay):
    def __init__(self, pin, active_high=True, initial_value=False):
        OFRelay.__init__(pin=pin, active_high=active_high, initial_value=initial_value)


