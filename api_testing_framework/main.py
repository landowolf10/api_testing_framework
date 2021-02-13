from api_methods.api_methods import APIMethods
from config.cfg import getURL

class TestCases():
    def __init__(self):
        super().__init__()

        self.api = APIMethods() 
        self.url = getURL()

    def get_content(self):
        if self.url[0] == False:
            status = self.api.validate_status_code(self.url[1])

            if status == 200:
                request_content = self.api.get_method(self.url[1])

                print(request_content["headers"])
                print("")
                print(request_content["response_content"])

tc = TestCases()

tc.get_content()