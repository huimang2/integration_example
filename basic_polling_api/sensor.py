보"""basic_polling_api 통합 구성요소의 sensor 플랫폼"""
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity

from .api import polling_api as API

# 1초에 한번씩 polling(기본값 설정)
SCAN_INTERVAL = timedelta(seconds=1)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """basic_polling_api 통합 구성요소의 플랫폼 Entry 설정"""

    api = API()

    # 개체(entity) 생성
    async_add_entities([ConfigEntrySensor(api)], True)


class ConfigEntrySensor(SensorEntity):
    """센서의 표현"""

    def __init__(self, api):
        """센서 초기화"""
        self._state = None
        # entity에 api 연결
        self._api = api


    @property
    def name(self):
        """센서의 이름을 리턴"""
        return "Polling API"


    @property
    def state(self):
        """센서의 상태 리턴"""
        return self._api.state



    def update(self):
        """센서의 상태 업데이트"""
        self._api.update()

