"""basic_polling_api 통합 구성요소의 Polling API"""

class polling_api:
    
    def __init__(self):
        """초기화"""
        self.state = None

    def update(self):
        f = open('/config/custom_components/basic_polling_api/state.txt','r')
        self.state = f.read()
        f.close()
