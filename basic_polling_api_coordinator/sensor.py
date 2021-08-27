"""basic_polling_api_coordinator 통합 구성요소의 sensor 플랫폼"""
from datetime import timedelta
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity


async def async_setup_entry(hass, entry, async_add_entities):
    """basic_polling_api_coordinator 통합 구성요소의 플랫폼 Entry 설정"""

    scan_interval = int(entry.data.get("scan_interval", 30))

    # coordinator 콜백함수
    async def async_get_data():

        f = open('/config/custom_components/basic_polling_api_coordinator/state.txt','r')
        state = f.read()
        f.close()

        return {"state":state}
    
    # coordinator 생성
    coordinator = DataUpdateCoordinator(
        hass,
        logging.getLogger(__name__),
        name=entry.data.get("title"),
        update_method=async_get_data,
        update_interval=timedelta(seconds=scan_interval),
    )

    await coordinator.async_config_entry_first_refresh()
    
    # 개체(entity) 생성
    async_add_entities([CoordinatorSensor(coordinator,entry)])


class CoordinatorSensor(CoordinatorEntity, SensorEntity):
    """센서의 표현"""

    def __init__(self,coordinator,entry):
        """센서 초기화"""
        super().__init__(coordinator)
        self._state = None
        self._title = entry.data.get("title")
        self._attr_unique_id = self._title


    @property
    def name(self):
        """센서의 이름을 리턴"""
        return self._title


    @property
    def state(self):
        """센서의 상태 리턴"""
        return self.coordinator.data.get('state')
