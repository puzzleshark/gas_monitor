from homeassistant import config_entries

# class GasMonitorConfigFlow(config_entries.ConfigFlow, domain="gas_monitor"):
#     async def async_step_user(self, user_input=None):
#         # This is the configuration step. 
#         # You can use `user_input` to get the data from the YAML file.
#         # This function should return a dict like this:
#         return self.async_create_entry(title="Gas Monitor", data=user_input)

import voluptuous as vol

class GasMonitorConfigFlow(config_entries.ConfigFlow, domain="gas_monitor"):
    async def async_step_user(self, info):
        if info is not None:
            pass

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("mac"): str})
        )