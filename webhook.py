import requests
import json


def webhook_events(name, data):
    webhook_url = ""

    webhook_data = {
        name:data
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(webhook_data),
                                 headers={'Content-Type': 'application/json'})
        
    except BaseException as e:
        print(e)


if __name__=="__main__":
    data={
        'hello':'world'
    }
    
    webhook_events("Test data",data)