# imports
import pandas as pd
import numpy as np
from datetime import datetime
from pi.co2_sensor import MHZ19
from pi.humidity_sensor import BME280


class Environment:
    def __init__(self, env_data, max_rows=86400, init_rows=80000, hum_temp=None, co2=None):

        self.max_rows = max_rows
        self.init_rows = init_rows

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
    def start_capture(cls, max_rows=5000, init_rows=4995, freq='5s'):
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
        data = np.tile(data, (init_rows, 1))

        index = pd.date_range(
            start=datetime.now() - (pd.Timedelta(freq) * (init_rows - 1)),
            end=datetime.now(),
            freq=freq
        )

        cols = ["temp", "humidity", "co2"]

        df = pd.DataFrame(data=data, index=index, columns=cols)

        return cls(df, max_rows, init_rows, hum_temp=hum_temp_sens, co2=co_sens)

    def get_sample(self):
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

        new_df = pd.concat([self.data, df])

        num_rows = new_df.shape[0]

        if num_rows == self.max_rows:
            new_df = new_df[-self.init_rows:]
        elif num_rows > self.max_rows:
            raise Exception('the number of rows should never get above the max allowable')

        self.data = new_df

        return df


