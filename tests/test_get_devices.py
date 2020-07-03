from cityair_api import CAR
import pandas as pd


class TestGetDevices:
    r = CAR(verify_ssl=False)

    def test_device_list(self):
        serials = self.r.get_devices()
        assert isinstance(serials, list)

    def test_devices_df(self):
        df = self.r.get_devices(format='df')
        assert isinstance(df, pd.DataFrame)