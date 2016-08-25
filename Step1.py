################################################################
## Query what endpoints are available
## Not all API's provide this capability,ex: ScaleIO doesn't
## Make sure you put the IP address of the XMS
## What's up with the Verify = False?

import requests
##xms = "https://192.168.0.7:54443"
xms = "https://192.168.184.129"
uri = "/api/json/v2/types"
url = xms + uri
response = requests.get(url, auth=('admin', 'Xtrem10'), verify=False)
print response.content

###############################################################
## This is an alternative way if you don't want to store passwd
##
## headers = { 'Authorization': 'Basic YWRtaW46WHRyZW0xMA==' }
## response = requests.get(url, headers=headers, verify=False)
