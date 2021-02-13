import requests
import json

#Clase para retornar request y otra para response

class APIMethods():
    def validate_status_code(self, url):
        status_code = self.get_method(url)["status_code"]
        status = None

        if status_code == 200:
            status = 200
            print("Ok!")
        elif status_code == 400:
            status = 400
            print("Bad Request!")
        elif status_code == 403:
            status = 403
            print("Forbidden!")
        elif status_code == 404:
            status = 404
            print("Not Found!")
        elif status_code == 405:
            status = 405
            print("Method Not Allowed!")
        elif status_code == 408:
            status = 408
            print("Request Timeout!")
        elif status_code == 500:
            status = 500
            print("Internal Server Error!")
        elif status_code == 502:
            status = 502
            print("Bad Gateway!")

        return status

    #TO DO: add more functionality
    def get_method(self, url):
        response = requests.get(url)

        statusCode = response.status_code
        headers = response.headers
        responseContent = json.loads(response.text)

        requests_object = {
            "status_code": statusCode,
            "headers": headers,
            "response_content": responseContent
        }

        return requests_object

    #TO DO: add POST method


    #TO DO: add PUT method


    #TO DO: add DELETE method