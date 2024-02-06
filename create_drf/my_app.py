import requests
import json

URL ="http://127.0.0.1:8000/stuinfo/"

data ={
  'name':'sonam',
  'city':'chittagong',
  'roll':101
}

json_data = json.dumps(data)

res = requests.post(url=URL, data=json_data)

data= res.json()
print(data)