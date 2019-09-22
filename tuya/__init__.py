from tuyapy import TuyaApi


class Tuya:

    def __init__(self, username, password, location, device):
        tuyaapi = TuyaApi()
        tuyaapi.init(
            username=username,
            password=password,
            countryCode=location
        )
        self.device = tuyaapi.get_device_by_id(device)