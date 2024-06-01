# imports
from pi.on_off_relay import OFRelay
from pi.pwm import PWM


class Humidifier:
    def __init__(
            self,
            fog_pin,
            fan_pin,
            fog_active_high=True,
            fan_active_high=True,
            fog_initial_value=False,
            fan_initial_dc_value=0,
            fan_pwm_freq=25000
    ):

        self.fogger = OFRelay(
            pin=fog_pin,
            active_high=fog_active_high,
            initial_value=fog_initial_value
        )

        self.hum_fan = PWM(
            pin=fan_pin,
            active_high=fan_active_high,
            initial_dc_value=fan_initial_dc_value,
            frequency=fan_pwm_freq
        )


