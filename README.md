# Tuya Smart Scale Custom Integration for Home Assistant

This integration is designed to retrieve weight (in kilograms) and other sensor data from a smart scale device that is not supported by the official Tuya integration in Home Assistant.

To use it, upload all the files into the custom_components/tuya_scale folder inside your Home Assistant configuration directory. 

Once the files are in place, you must restart Home Assistant before proceeding. After the restart, you can add your device by selecting "Add Integration" from the Home Assistant interface.

Please note that you will need your API credentials in order to add and connect your devices successfully.


---

## File Structure

Make sure your folder structure looks like this:
```
custom_components/
    └── tuya_scale/
        ├── init.py
        ├── binary_sensor.py
        ├── config_flow.py
        ├── const.py
        ├── coordinator.py
        ├── manifest.json
        ├── sensor.py
        ├── strings.json
        ├── translations/
            ├── en.json
            └── tr.json
        └── README.md

```
