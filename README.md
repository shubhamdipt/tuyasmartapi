# tuyasmartapi
An api for handling Tuya Smart devices.

## Dependencies
Python3

    pip install -r requirements.txt


## Usage

Create a config.ini file with the following contents.

    [TUYA]
    username = <username>
    password = <password>
    location = EU
    device = <device_id>

## Installation

    pip install tuyasmartapi

### Example

    >>>from tuya.devices.tuya_smart_plug import TuyaSmartSwitch
    >>>device = TuyaSmartSwitch(username=CONFIG["TUYA"]["username"], password=CONFIG["TUYA"]["password"], location=CONFIG["TUYA"]["location"], device=CONFIG["TUYA"]["device"])
    >>>print(device.get_status())
