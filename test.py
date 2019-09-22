from devices.tuya_smart_plug import TuyaSmartSwitch
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


if __name__ == "__main__":
    device = TuyaSmartSwitch(
        username=CONFIG["TUYA"]["username"],
        password=CONFIG["TUYA"]["password"],
        location=CONFIG["TUYA"]["location"],
        device=CONFIG["TUYA"]["device"],
    )
    print(device.get_status())
