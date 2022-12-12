from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# Create your views here.
def route(request):
    url="https://graphhopper.com/api/1/vrp?key=38271ad0-121c-4b59-9e50-83f1b60866fc"
    payload = json.dumps({
  "vehicles": [
    {
      "vehicle_id": "my_vehicle",
      "start_address": {
        "location_id": "MCP2",
        "lat": 10.7716128,
        "lon": 106.6592997
      }
    }
    ],
  "services": [
    {
      "id": "Cơ_sở_2",
      "name": "Cơ_sở_2",
      "address": {
        "location_id": "MCP1",
        "lat": 10.8799198, 
        "lon": 106.8047006
      }
    },
    {
      "id": "Quận_11",
      "name": "Nhân_viên_Sơn",
      "address": {
        "location_id": "MCP3",
        "lat": 10.7711526, 
        "lon": 106.6529604
      }
    }
    ]
    })
    headers = {
  'Content-Type': 'application/json'
    }   

    response = requests.request("POST", url, headers=headers, data=payload)#response in json format
    route=(response.json()) #dict format
    mes=""
    for i in route['solution']['routes'][0]['activities']: #get the order of visting node
        mes+=' -> '+i['location_id'] #display order of MCP
    mes=mes[4:]
    print(mes)

    return JsonResponse(response.json())
# Create your views here.