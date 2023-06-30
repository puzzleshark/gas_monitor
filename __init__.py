import logging
import re

from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator

_LOGGER = logging.getLogger()


DOMAIN = "gas_monitor"

def my_parser(service_info: BluetoothServiceInfoBleak):
    _LOGGER.info(service_info)
    return service_info.name


async def async_setup(hass, config):
    _LOGGER.info(config)
    hass.states.async_set("gas_monitor.percentage", "hi")

    def my_parser(service_info: BluetoothServiceInfoBleak):
        _LOGGER.info(service_info)
        match = re.search(r'trbl:ACC \((.*?)\)', service_info.name)
        if match:
            value = match.group(1)
            print("Value in parentheses: ", value)
            hass.states.async_set("gas_monitor.percentage", float(value))
        return service_info.name

    coordinator = PassiveBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address="F4:55:1D:09:DC:34",
        mode=BluetoothScanningMode.ACTIVE,
        update_method=my_parser
    )
    coordinator.async_start()

    return True
