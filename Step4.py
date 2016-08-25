################################################################
## Query the Volumes endpoint, to ask about the LUN we just created
## Can you extract specific data of the new volume from output?
## Make sure you put the IP address of the XMS

import requests

##xms = "https://192.168.0.7:54443"
xms = "https://192.168.184.129"
uri = "/api/json/v2/types/volumes/4"
url = xms + uri
response = requests.get(url, auth=('admin', 'Xtrem10'), verify=False)
print response.content
