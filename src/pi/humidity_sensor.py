# imports
import bme280
from smbus2 import SMBus


class BME280:
    def __init__(self, port=1, address=0x76, calibration_params=None):
        self.port = port,
        self.address = address
        self.bus = SMBus(port)

        if calibration_params is None:
            self.calibration_params = bme280.load_calibration_params(self.bus, address)
        else:
            self.calibration_params = calibration_params

    def get_sample(self):
        sample = bme280.sample(bus=self.bus, address=self.address, compensation_params=self.calibration_params)

        return {
            "time": sample.timestamp,
            "temp": (sample.temperature * (9/5)) + 32,
            "humidity": sample.humidity
                }
