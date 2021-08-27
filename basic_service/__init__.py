"""basic_service 통합 구성요소 컴포넌트"""

from .const import DOMAIN, ATTR_TEXT, DEFAULT_NAME


def setup(hass, config):
    """basic_service 통합 구성요소 컴포넌트 설정"""

    def handle_service(call):
        """서비스콜 처리 """
        hass.states.set(f"{DOMAIN}.service", call.data.get(ATTR_TEXT, DEFAULT_NAME))
    
    # 서비스 등록
    hass.services.register(DOMAIN, "call_service", handle_service)
    
    # 초기값 설정
    hass.states.set(f"{DOMAIN}.service", DEFAULT_NAME)

    return True
