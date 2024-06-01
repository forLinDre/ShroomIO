# imports
from pi.on_off_relay import OFRelay


class FAE(OFRelay):
    def __init__(self, pin, active_high=True, initial_value=False):
        OFRelay.__init__(
            self, pin=pin,
            active_high=active_high,
            initial_value=initial_value
        )