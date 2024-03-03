# imports
from on_off_relay import OFRelay


class Heater(OFRelay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)