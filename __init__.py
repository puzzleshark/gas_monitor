import logging
import re

from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothProcessorCoordinator

_LOGGER = logging.getLogger("custom_components.gas_monitor")


DOMAIN = "gas_monitor"

def my_parser(service_info: BluetoothServiceInfoBleak):
    _LOGGER.info(service_info)
    return service_info.name


async def async_setup(hass, config):
    _LOGGER.info(config)

    def my_parser(service_info: BluetoothServiceInfoBleak):
        _LOGGER.info(service_info)
        match = re.search(r'trbl:ACC \((.*?)\)', service_info.name)
        if match:
            # bluetooth device advertises different names, we only care when the name has the percentage in it
            value = match.group(1)
            hass.states.async_set("gas_monitor.percentage", float(value))

    coordinator = PassiveBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address=config["gas_monitor"]["mac"],
        mode=BluetoothScanningMode.ACTIVE,
        update_method=my_parser
    )
    coordinator.async_start()

    return True
