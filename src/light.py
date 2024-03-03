# imports
from pi.on_off_relay import OFRelay


class Light(OFRelay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


