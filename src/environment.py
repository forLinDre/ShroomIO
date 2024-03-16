# imports
import pandas as pd
import numpy as np
from datetime import datetime
from pi.co2_sensor import MHZ19
from pi.humidity_sensor import BME280


class Environment:
    def __init__(self, env_data):
        self.data = env_data

    @classmethod
    def start_capture(cls, rows=20, increment='5s'):
        co_read = MHZ19.get_sample()
        hum_temp_read = BME280.get_sample()
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

        return cls(df)

    def get_sample(self, max_rows=200):
        co_read = MHZ19.get_sample()
        hum_temp_read = BME280.get_sample()
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

