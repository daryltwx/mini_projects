import requests
from datetime import datetime

USERNAME = "roger44221"
TOKEN = "thisissecret"
GRAPH_ID = "graph1"
today_date = datetime(year=2023, month=11, day=8).strftime("%Y%m%d")
DATE = datetime.now().strftime("%Y%m%d")

QUANTITY = "10"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes", 
    "thanksCode": "ThisIsThanksCode"
}


## ---------------------- Create Account -----------------------------
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": "graph1",
  "name": "Cycling Graph",
  "unit": "km", 
  "type": "float",
  "color": "ajisai",
}

headers = {
  "X-USER-TOKEN": TOKEN
}

## -------------------------------- Create Graph --------------------------

#graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(graph_response.text)

## -------------------- Add Pixel -----------------------
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
  "date": today_date,
  "quantity": QUANTITY,
}

#pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(pixel_response.text)



## --------------------------------------- Delete pixel ---------------------

pixel_update_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"

# delete_response = requests.delete(url=pixel_update_delete_endpoint, headers=headers)
# print(delete_response.text)



## --------------------------------------- Update Pixel ---------------------
update_config = {
  "quantity": "20"
}

update_response = requests.put(url=pixel_update_delete_endpoint, json=update_config, headers=headers)
print(update_response.text)
