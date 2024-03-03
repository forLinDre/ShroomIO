# imports
from src.pi.on_off_relay import OFRelay


class FAE(OFRelay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)