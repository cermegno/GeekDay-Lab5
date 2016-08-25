################################################################
## Query the Volumes endpoint, to ask about its inventory
## Make sure you put the IP address of the XMS
## Now change the code to see cluster and initiator information

import requests
##xms = "https://192.168.0.7:54443"
xms = "https://192.168.184.129"
uri = "/api/json/v2/types/volumes"
url = xms + uri
response = requests.get(url, auth=('admin', 'Xtrem10'), verify=False)
print response.content
