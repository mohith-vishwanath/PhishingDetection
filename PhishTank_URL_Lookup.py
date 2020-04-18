import requests
import json

class phishTank:

    #PARAMETERS
    request_url = ""
    format = "json"
    api_key = "b3a0f62cccc67e5c6addeaa4b2b7631fc6f9851891ef9e2da1548eb967674d47"

    send_request_to_url = "http://checkurl.phishtank.com/checkurl/"

    def __init__(self, url):
        self.request_url = url

    def isURLFake(self):

        parameters = {
            'url' : self.request_url,
            'format' : self.format,
            'app_key' : self.api_key
        }

        response = requests.post("http://checkurl.phishtank.com/checkurl/index.php?url=http://.google.com")
        print(response.content.)


obj = phishTank("www.gooogle.com")
obj.isURLFake()
