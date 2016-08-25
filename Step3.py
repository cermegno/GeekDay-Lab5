################################################################
## Creating a new volume. What HTTP operation do we need?
## Make sure you put the IP address of the XMS
## NOTE: The whole class will be attempting to create volumes
## You might be creating a volume with a name that exist already
## How do you check whether the operation completed successfully

import requests
import json

##xms = "https://192.168.0.7:54443"
xms = "https://192.168.184.129"
uri = "/api/json/v2/types/volumes"
url = xms + uri
vol_details = {"vol-name":"MyVol2","vol-size":"10G"}
response = requests.post(url, data=json.dumps(vol_details), auth=('admin', 'Xtrem10'), verify=False)
print response.content
