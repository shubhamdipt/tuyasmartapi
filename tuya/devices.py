from tuya import Tuya


class TuyaSmartSwitch(Tuya):

    def get_status(self):
        return self.device.state()

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()