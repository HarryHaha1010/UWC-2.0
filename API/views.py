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
        "location_id": "berlin",
        "lon": 13.406,
        "lat": 52.537
      }
    }
  ],
  "services": [
    {
      "id": "hamburg",
      "name": "visit_hamburg",
      "address": {
        "location_id": "hamburg",
        "lon": 9.999,
        "lat": 53.552
      }
    },
    {
      "id": "munich",
      "name": "visit_munich",
      "address": {
        "location_id": "munich",
        "lon": 11.57,
        "lat": 48.145
      }
    }
    ]
    })
    headers = {
  'Content-Type': 'application/json'
    }   

    response = requests.request("POST", url, headers=headers, data=payload)

    return JsonResponse(response.json())
# Create your views here.
