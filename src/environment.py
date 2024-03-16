# imports
import pandas as pd
import numpy as np
from datetime import datetime
from pi.co2_sensor import MHZ19
from pi.humidity_sensor import BME280


class Environment:
    def __init__(self, env_data, hum_temp=None, co2=None):
        if hum_temp is not None:
            self.hum_temp = hum_temp
        else:
            self.hum_temp = BME280()

        if co2 is not None:
            self.co2 = co2
        else:
            self.co2 = MHZ19()

        self.data = env_data

    @classmethod
    def start_capture(cls, rows=20, increment='5s'):
        hum_temp_sens = BME280()
        co_sens = MHZ19()
        co_read = co_sens.get_sample()
        hum_temp_read = hum_temp_sens.get_sample()
        # co_read = {"co2": 1648}
        # hum_temp_read ={
        #     "time": datetime.now(),
        #     "temp": 45.5,
        #     "humidity": 71.3
        #         }

        data = np.array([hum_temp_read.get("temp"), hum_temp_read.get("humidity"), co_read.get("co2")])
        data = np.tile(data, (rows, 1))

        index = pd.date_range(
            start=datetime.now() - (pd.Timedelta(increment) * (rows - 1)),
            end=datetime.now(),
            freq=increment
        )

        cols = ["temp", "humidity", "co2"]

        df = pd.DataFrame(data=data, index=index, columns=cols)

        return cls(df, hum_temp=hum_temp_sens, co2=co_sens)

    def get_sample(self, max_rows=200):
        co_read = self.co2.get_sample()
        hum_temp_read = self.hum_temp.get_sample()
        # co_read = {"co2": 1600}
        # hum_temp_read ={
        #     "time": datetime.now(),
        #     "temp": 35.5,
        #     "humidity": 61.3
        #         }

        data = np.array([[hum_temp_read.get("temp"), hum_temp_read.get("humidity"), co_read.get("co2")]])

        index = pd.DatetimeIndex([datetime.now()])
        cols = ["temp", "humidity", "co2"]
        df = pd.DataFrame(data=data, index=index, columns=cols)

        self.data = pd.concat([self.data, df])

