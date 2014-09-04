import json
import requests
import config


# get measurements from apis function.
def get_measurements():
    return json.loads(requests.get(url=config.APIS_URL).text)