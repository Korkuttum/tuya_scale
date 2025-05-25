# Tuya Smart Scale Custom Integration for Home Assistant

This integration is designed to retrieve weight (in kilograms) and other sensor data from a smart scale device that is not supported by the official Tuya integration in Home Assistant.

## Installation Methods

### Method 1: HACS Installation (Recommended)
1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance.
2. Click on `HACS` in the sidebar.
3. Click on the three dots in the top right corner and select `Custom Repositories`.
4. Add this repository URL `https://github.com/Korkuttum/tuya_scale` and select `Integration` as the category.
5. Click `ADD`.
6. Find and click on "Tuya Smart Scale" in the integrations list.
7. Click `Download` and install it.
8. Restart Home Assistant.

### Method 2: Manual Installation
To install manually, upload all the files into the custom_components/tuya_scale folder inside your Home Assistant configuration directory. 

## Configuration

Once installed (either through HACS or manually), you must restart Home Assistant before proceeding. After the restart, you can add your device by selecting "Add Integration" from the Home Assistant interface.

Please note that you will need your API credentials in order to add and connect your devices successfully.

---

## File Structure

Make sure your folder structure looks like this (if installing manually):
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
