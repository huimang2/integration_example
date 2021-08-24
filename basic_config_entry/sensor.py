"""basic_config_entry 통합 구성요소의 sensor 플랫폼"""
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity

from . import DOMAIN

# 1초에 한번씩 polling
SCAN_INTERVAL = timedelta(seconds=1)


async def async_setup_entry(hass, entry, async_add_entities):
    """basic_config_entry 통합 구성요소의 sensor 플랫폼 Entry 설정"""

    # 개체(entity) 생성
    async_add_entities([ConfigEntrySensor(entry)])


class ConfigEntrySensor(SensorEntity):
    """센서의 표현"""

    def __init__(self,entry):
        """센서 초기화"""
        self._state = None
        # 전달받은 entry에서 'text'키(key)의 값(value)출력
        self._text = entry.data.get('text')
        # unique_id 설정
        self._attr_unique_id = f"{self._text}"

    @property
    def name(self):
        """센서의 이름을 리턴"""
        return 'text Entry'

    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._state


    def update(self):
        """센서의 상태 업데이트"""
        self._state = self._text

