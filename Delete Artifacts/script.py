import requests

# url = "https://artifactory.comcast.com/artifactory/xmdp-docker/xm-dp/xmdmportal/test/xmdmcustomermoves/1.0.12"


payload={}
headers = {
    'Authorization': 'Basic TOKEN'
    }

file = open('data.txt', 'r')
for i, data in enumerate(file.readlines()):
    print(i+1)
    response = requests.request("DELETE", data, headers=headers, data=payload)
    if not (response.text == ""):
        print(data)
    
