# Tuya Smart Scale Custom Integration for Home Assistant

<img src="https://iis-akakce.akamaized.net/p.z?%2F%2Fproductimages%2Ehepsiburada%2Enet%2Fs%2F45%2F600%2F10824497070130%2Ejpg" alt="Smart Scale" width="200"/> <img src="https://image.made-in-china.com/2f0j00aMhREsrtVIbv/Tuya-Smart-Body-Weighing-Scales.webp" alt="Smart Scale" width="200"/> <img src="https://www.expert4house.com/img/cms/Tuya%20Smart%20Home/Tuya%20Bilancia%20del%20Grasso%20Corporeo%20BMI%20Smart%20WiFi%20con%20Display%20Digitale%20a%20LED.jpg" alt="Smart Scale" width="200"/>


This integration is designed to retrieve weight (in kilograms) and other sensor data from a smart scale device that is not supported by the official Tuya integration in Home Assistant.

## Installation Methods

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Korkuttum&repository=tuya_scale&category=integration)

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

---

## Support My Work

If you find this integration helpful, consider supporting the development:

[![Become a Patreon](https://img.shields.io/badge/Become_a-Patron-red.svg?style=for-the-badge&logo=patreon)](https://www.patreon.com/c/korkuttum)
