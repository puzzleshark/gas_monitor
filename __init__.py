DOMAIN = "gas_monitor"


# def setup(hass, config):
#     hass.states.set("gas_monitor.world", "Paulus")

#     # Return boolean to indicate that initialization was successful.
#     return True


import logging
from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import (
    PassiveBluetoothProcessorCoordinator,
)
from homeassistant.const import Platform

PLATFORMS: list[Platform] = [Platform.SENSOR]
_LOGGER = logging.getLogger(__name__)


def my_parser(service_info: BluetoothServiceInfoBleak):
    _LOGGER.log(service_info)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up example BLE device from a config entry."""
    address = entry.unique_id
    coordinator = hass.data.setdefault(DOMAIN, {})[
        entry.entry_id
    ] = PassiveBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address=address,
        mode=BluetoothScanningMode.ACTIVE,
        update_method=data.update,
    )
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(
        # only start after all platforms have had a chance to subscribe
        coordinator.async_start()
    )
    return True