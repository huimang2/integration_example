"""basic_platform_schema 통합 구성요소의 sensor 플랫폼"""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity

from .const import DOMAIN, CONF_TEXT, DEFAULT_TEXT


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_TEXT, default=DEFAULT_TEXT) : cv.string
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """basic_platform_schema 통합 구성요소 플랫폼 설정"""

    add_entities([SchemaSensor(config)])


class SchemaSensor(SensorEntity):
    """센서의 표현"""

    def __init__(self,config):
        """센서 초기화"""
        self._state = config.get(CONF_TEXT)

    @property
    def name(self):
        """센서의 이름을 리턴"""
        return '플랫폼 스키마 예제'

    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._state