"""The Tuya Scale integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS
from .coordinator import TuyaScaleDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Tuya Scale from a config entry."""
    coordinator = TuyaScaleDataUpdateCoordinator(hass, entry)
    await coordinator.async_refresh()  # async_config_entry_first_refresh yerine

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    # Use async_forward_entry_setups instead of async_forward_entry_setup
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok