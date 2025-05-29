"""Constants for the Tuya Scale integration."""
from datetime import timedelta
from homeassistant.const import (
    Platform,
    UnitOfMass,
)

DOMAIN = "tuya_scale"
PLATFORMS = [Platform.SENSOR]
# Eski SCAN_INTERVAL sabitini kaldırıp yerine aşağıdaki iki satırı ekliyoruz
DEFAULT_SCAN_INTERVAL = 1  # Varsayılan değer (dakika cinsinden)
CONF_SCAN_INTERVAL = "scan_interval"  # Yeni yapılandırma sabiti

# Configuration
CONF_ACCESS_ID = "access_id"
CONF_ACCESS_KEY = "access_key"
CONF_DEVICE_ID = "device_id"
CONF_REGION = "region"

# API Region
DEFAULT_REGION = "EU"
REGIONS = {
    "EU": "https://openapi.tuyaeu.com",
    "US": "https://openapi.tuyaus.com",
    "CN": "https://openapi.tuyacn.com",
    "IN": "https://openapi.tuyain.com"
}

# API Paths
TOKEN_PATH = "/v1.0/token?grant_type=1"
DEVICE_DATA_PATH = "/v2.0/cloud/thing/{device_id}/shadow/properties"

# Device Info
DEFAULT_NAME = "Tuya Smart Scale"
DEFAULT_MANUFACTURER = "Tuya"
DEFAULT_MODEL = "Smart Scale"

# Measurement Units
UNIT_RESISTANCE = "Ω"

# Error Messages
ERROR_AUTH = "Authentication failed"
ERROR_CONN = "Failed to connect"
ERROR_TIMEOUT = "Connection timeout"

# Current values
CURRENT_USER = "Korkuttum"
CURRENT_TIME = "2025-05-29 14:10:10"

# Sensor Types
SENSOR_TYPES = {
    "weight": {
        "key": "weight",
        "name": "Weight",
        "unit": UnitOfMass.GRAMS,
        "icon": "mdi:scale-bathroom",
        "device_class": "weight",
        "state_class": "measurement",
    },
    "body_resistance": {
        "key": "BR",
        "name": "Body Resistance",
        "unit": UNIT_RESISTANCE,
        "icon": "mdi:omega",
        "state_class": "measurement",
    },
    "weight_count": {
        "key": "weightcount",
        "name": "Measurement Count",
        "icon": "mdi:counter",
        "state_class": "total_increasing",
    },
    "left_resistance": {
        "key": "LResistance",
        "name": "Left Resistance",
        "unit": UNIT_RESISTANCE,
        "icon": "mdi:omega",
        "state_class": "measurement",
    },
    "right_high_resistance": {
        "key": "RHR",
        "name": "Right High Resistance",
        "unit": UNIT_RESISTANCE,
        "icon": "mdi:omega",
        "state_class": "measurement",
    },
    "left_low_resistance": {
        "key": "LLR",
        "name": "Left Low Resistance",
        "unit": UNIT_RESISTANCE,
        "icon": "mdi:omega",
        "state_class": "measurement",
    },
    "right_low_resistance": {
        "key": "RLR",
        "name": "Right Low Resistance",
        "unit": UNIT_RESISTANCE,
        "icon": "mdi:omega",
        "state_class": "measurement",
    },
    "battery": {
        "key": "battery",
        "name": "Battery Status",
        "icon": "mdi:battery",
        "device_class": "battery",
    },
}
