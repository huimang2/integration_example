"""basic_config_entry 통합 구성요소 컴포넌트"""
from .const import DOMAIN, PLATFORMS


async def async_setup_entry(hass, entry):
    """basic_config_entry 통합 구성요소 Entry 설정"""
    
    # Entry를 플랫폼으로 전달
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass, entry):
    """basic_config_entry 통합 구성요소 Entry 제거"""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
