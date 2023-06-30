from dataclasses import dataclass
import logging

from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator
from homeassistant.const import Platform

_LOGGER = logging.getLogger(__name__)


DOMAIN = "gas_monitor"

def my_parser(service_info: BluetoothServiceInfoBleak):
    _LOGGER.info(service_info)
    return service_info.name


# def setup(hass, config):
#     hass.states.set("gas_monitor.value", 10)

#     # Return boolean to indicate that initialization was successful.
#     return True

def async_setup(hass, config):
    _LOGGER.info(config)
    hass.states.async_set("gas_monitor.percentage", 10)

    coordinator = PassiveBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address="F4:55:1D:09:DC:34",
        mode=BluetoothScanningMode.ACTIVE,
        update_method=my_parser
    )
    coordinator.async_start()

    # Return boolean to indicate that initialization was successful.
    return True
    


# from dataclasses import dataclass
# import logging

# from home_assistant_bluetooth import BluetoothServiceInfoBleak
# from homeassistant.config_entries import ConfigEntry
# from homeassistant.const import Platform
# from homeassistant.core import HomeAssistant
# from homeassistant.components.bluetooth import BluetoothScanningMode
# from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator
# from homeassistant.const import Platform

# PLATFORMS: list[Platform] = [Platform.SENSOR]
# _LOGGER = logging.getLogger(__name__)

# @dataclass
# class my_data_class:
#     value: str


# def my_parser(service_info: BluetoothServiceInfoBleak):
#     _LOGGER.log(service_info)
#     return service_info.name

# async def async_setup_entry(hass: HomeAssistant, config) -> bool:
#     """Set up example BLE device from a config entry."""
#     coordinator = PassiveBluetoothProcessorCoordinator(
#         hass,
#         _LOGGER,
#         address="F4:55:1D:09:DC:34",
#         mode=BluetoothScanningMode.ACTIVE,
#         update_method=my_parser
#     )
#     coordinator.async_start()


#     # address = entry.unique_id
#     # coordinator = hass.data.setdefault(DOMAIN, {})[
#     #     entry.entry_id
#     # ] = PassiveBluetoothProcessorCoordinator(
#     #     hass,
#     #     _LOGGER,
#     #     address=address,
#     #     mode=BluetoothScanningMode.ACTIVE,
#     #     update_method=my_parser,
#     # )
#     # await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
#     # entry.async_on_unload(
#     #     # only start after all platforms have had a chance to subscribe
#     #     coordinator.async_start()
#     # )
#     return True