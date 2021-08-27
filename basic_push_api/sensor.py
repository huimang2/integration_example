"""basic_push_api 통합 구성요소의 sensor 플랫폼"""
import voluptuous as vol

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers import entity_platform
from homeassistant.helpers.dispatcher import (async_dispatcher_connect, async_dispatcher_send)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """basic_push_api 통합 구성요소의 플랫폼 설정"""
    
    # 서비스 추가
    platform = entity_platform.async_get_current_platform()
    platform.async_register_entity_service("get_state", {vol.Required("text"): str}, "async_get_state")
    
    # entity 추가
    async_add_entities([PushSensor()])


class PushSensor(SensorEntity):
    """센서의 표현"""

    def __init__(self):
        """센서 초기화"""
        self._state = None


    async def async_added_to_hass(self):
        """entity가 생성될때 호출"""
        async def async_update_state(text):
            """dispatcher 콜백 함수"""
            # update 콜백을 실행하여 state 업데이트
            self._state = text
            await self.async_write_ha_state()

        # dispatcher 연결(구독)
        self._dispatcher_remove = async_dispatcher_connect(
            self.hass, "update", async_update_state)


    async def async_will_remove_from_hass(self):
        """entity가 제거될때 호출"""
        # dispatcher 해제(구독 취소)
        if self._dispatcher_remove:
            self._dispatcher_remove()


    @property
    def name(self):
        """센서의 이름을 리턴"""
        return 'Push API'


    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._state


    @property
    def should_poll(self) -> bool:
        """Polling이 필요하면 True, 필요없으면 False 리턴"""
        return False

    
    async def async_get_state(self, text):
        """서비스 실행시 데이터 전송(push API)"""
        async_dispatcher_send(self.hass, "update", text)
