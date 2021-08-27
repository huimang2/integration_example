"""
최소한의 형태의 통합 구성요소 입니다.
configuration.yaml 파일에 다음 구문을 추가해주세요.

basic_async:
"""

# 도메인은 통합 구성요소의 디렉토리명과 같아야합니다.
DOMAIN = "basic_async"


async def async_setup(hass, config):
    """basic_async 통합 구성요소 컴포넌트 설정"""
    # 상태(States)는 DOMAIN.OBJECT_ID 형식으로 설정됩니다.
    hass.states.async_set('basic_async.hellow_world', '작동!')

    # 초기화에 성공화면 True를 리턴합니다.
    return True
