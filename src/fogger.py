# imports
from on_off_relay import OFRelay


class Fogger(OFRelay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)