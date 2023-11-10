import requests

nurtri_endpoint = 'https://trackapi.nutritionix.com/'
nurtri_api_key = 'your_api_key'


APP_ID = "cb6cec39"
APP_KEY = "1dbe5d0f36dcaafeb4d0384fb52a50f0"

headers = {
  "x-app-id": APP_ID,
  "x-app-key": APP_KEY,
}

q = input("Tell me the exercise: ")

nurtri_params = {
  "query": q,
}

natural_endpoint = f"{nurtri_endpoint}/v2/natural/exercise"
exercise_response = requests.post(url=natural_endpoint, headers=headers, json=nurtri_params)
print(exercise_response.json())



## -------- Sheety -------------

username = "your_username"
projectName = "your_projectName"
sheetName = "your_sheetName"

sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

sheety_params = {
  "email": {
    "name": "Syed K",
    "email": "syed@gmail.com"
  }
}


## ------- 
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

