"""
최소한의 형태의 통합 구성요소 입니다.
configuration.yaml 파일에 다음 구문을 추가해주세요.

basic_schema:

"""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

# 상수 불러오기
from .const import DOMAIN, CONF_TEXT, DEFAULT_TEXT

# 컴포넌트 config 스키마 작성
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_TEXT, default=DEFAULT_TEXT) : cv.string
    }, extra=vol.ALLOW_EXTRA)
}, extra=vol.ALLOW_EXTRA)

def setup(hass, config):
    """basic_schema 통합 구성요소 설정"""
    hass.states.set(f'{DOMAIN}.schema', config[DOMAIN].get(CONF_TEXT))

    # 초기화에 성공화면 True를 리턴합니다.
    return True