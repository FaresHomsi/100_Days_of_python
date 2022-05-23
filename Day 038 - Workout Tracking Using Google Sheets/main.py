import requests
from datetime import datetime

GENDER = "Your Gender"
WEIGHT_KG = "Your Weight"
HEIGHT_CM = "Your Height"
AGE = "Your Age"

APP_ID = "Your App ID"
API_KEY = "Your API Key"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

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

sheety_endpoint = "https://api.sheety.co/b3870d1bbcfe48aa79ca45d3b115e962/workoutTracking/workouts"

sheety_headers = {
    "Authorization": "YOur Authorization Key"
}

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

print(sheet_response.text)

