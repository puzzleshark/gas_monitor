from homeassistant import config_entries

import voluptuous as vol

class GasMonitorConfigFlow(config_entries.ConfigFlow, domain="gas_monitor"):
    VERSION = 1
    # async def async_step_user(self, info):
    #     if info is not None:
    #         pass

    #     return self.async_show_form(
    #         step_id="user", data_schema=vol.Schema({vol.Required("mac"): str})
    #     )
    async def async_step_finish(self, user_input=None):
        return self.async_create_entry(title=self.data["title"], data=self.data)