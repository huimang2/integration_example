
"""
최소한의 형태의 통합 구성요소 입니다.
configuration.yaml 파일에 다음 구문을 추가해주세요.

basic_sync:
"""

# 도메인은 통합 구성요소의 디렉토리명과 같아야합니다.
DOMAIN = "basic_sync"


def setup(hass, config):
    """basic_sync 통합 구성요소 설정"""
    # 상태(States)는 DOMAIN.OBJECT_ID 형식으로 설정됩니다.
    hass.states.set('hello_world.Hello_World', 'Works!')

    # 초기화에 성공화면 True를 리턴합니다.
    return True