"""Config flow for Tuya Scale integration."""
from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from .const import (
    DOMAIN,
    CONF_ACCESS_ID,
    CONF_ACCESS_KEY,
    CONF_DEVICE_ID,
    CONF_REGION,
    REGIONS,
    DEFAULT_REGION,
)
from .coordinator import TuyaScaleDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ACCESS_ID): str,
        vol.Required(CONF_ACCESS_KEY): str,
        vol.Required(CONF_DEVICE_ID): str,
        vol.Required(CONF_REGION, default=DEFAULT_REGION): vol.In(REGIONS.keys()),
    }
)

async def validate_input(hass: HomeAssistant, data: dict) -> dict:
    """Validate the user input allows us to connect."""
    coordinator = TuyaScaleDataUpdateCoordinator(
        hass,
        type('MockConfigEntry', (), {'data': data})()
    )

    try:
        await coordinator.async_refresh()  # async_config_entry_first_refresh yerine
    except Exception as err:
        _LOGGER.error("Validation error: %s", err)
        raise CannotConnect from err

    return {"title": f"Tuya Scale ({data[CONF_DEVICE_ID]})"}

class TuyaScaleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tuya Scale."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(user_input[CONF_DEVICE_ID])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""

class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""