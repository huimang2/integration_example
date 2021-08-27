"""basic_platform 통합 구성요소의 sensor 플랫폼"""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity


def setup_platform(hass, config, add_entities, discovery_info=None):
    """basic_platform 통합 구성요소 플랫폼 설정"""
    add_entities([ExampleSensor()])


class ExampleSensor(Entity):
    """센서의 표현"""

    def __init__(self):
        """센서 초기화"""
        self._state = None

    @property
    def name(self):
        """센서의 이름을 리턴"""
        return '온도 예시'

    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._state

    @property
    def unit_of_measurement(self):
        """측정단위 리턴"""
        return TEMP_CELSIUS

    def update(self):
        """센서의 상태 업데이트"""
        self._state = 23

