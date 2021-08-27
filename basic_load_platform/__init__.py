"""basic_load_platform 통합 구성요소 컴포넌트"""
DOMAIN = 'basic_load_platform'


def setup(hass, config):
    """basic_load_platform 통합 구성요소 컴포넌트 설정"""
    # 플랫폼과 공유하기 원하는 데이터
    hass.data[DOMAIN] = {
        'temperature': 30
    }

    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True
