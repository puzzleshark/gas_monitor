# Home Assistant Otodata Fuel Tank Monitor Integration

Integration monitors the percentage of fuel in an otodata tank. Rather than using the dedicated app you can use this integration to display tank percentage within home-assistant.

## Setup

Add
```yaml
gas_monitor:
  - mac: xx:xx:xx:xx
```
to your **configuration.yaml**

where **mac** is the mac address of the bluetooth tank monitoring device.
