"""basic_polling_api_coordinator 통합 구성요소 컴포넌트"""
import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """basic_polling_api_coordinator 통합 구성요소 ConfigFlow """

    async def async_step_user(self, user_input):

        # UI에 표시되는 순서대로 항목 지정
        data_schema = {
            vol.Required("title"): str,
            vol.Optional("scan_interval"): int
        }
        
        if user_input is not None:
            """entry 생성"""
            return self.async_create_entry(title=user_input.get("title"), data=user_input)

        #사용자에게 입력할 양식 표시
        return self.async_show_form(step_id="user", data_schema=vol.Schema(data_schema))
