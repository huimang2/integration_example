"""basic_entity_service 통합 구성요소의 sensor 플랫폼"""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv, entity_platform
from homeassistant.components.sensor import SensorEntity

from .const import SERVICE_CALL_SERVICE, ATTR_TEXT, DEFAULT_TEXT


async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    """basic_entity_service 통합 구성요소 플랫폼 설정"""

    platform = entity_platform.async_get_current_platform()

    # 서비스 등록
    platform.async_register_entity_service(
        SERVICE_CALL_SERVICE,
        {
            vol.Optional(ATTR_TEXT, default=DEFAULT_TEXT): cv.string,
        },
        "set_state",
    )
    
    # 센서 추가
    add_entities([EntityServiceSensor()])


class EntityServiceSensor(SensorEntity):
    """센서의 표현"""

    def __init__(self):
        """센서 초기화"""
        self._state = DEFAULT_TEXT

    @property
    def name(self):
        """센서의 이름을 리턴"""
        return '구성요소 서비스 센서 예제'

    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._state

    def set_state(self, **kwargs):
        """센서 상태 변경 서비스"""
        self._state = kwargs.get(ATTR_TEXT)
