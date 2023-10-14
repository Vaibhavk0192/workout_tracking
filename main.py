import os
import dotenv
import requests
import datetime

dotenv.load_dotenv()
date=datetime.datetime.now()
time=date.strftime("%X")
date=date.strftime("%x")


API_ID=os.getenv('API_ID')
API_KEY=os.getenv('API_KEY')
AUTH=os.getenv('AUTH')


GENDER="Male"
WEIGHT_KG=69
HEIGHT_CM=169
AGE=21




api_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}

exercise_test=input("Tell me which execise you did: ")
parameters={
    "query":exercise_test,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
response=requests.post(api_endpoint,json=parameters,headers=headers)
result=response.json()


sheety_endpoint="https://api.sheety.co/b66a1a4492299556c1fc14e34a236d85/myWorkouts/workouts"
for exercise in result["exercises"]:

    parameters={
        
    "workout": {
        "date":date,
        "time":time,
        "exercise":exercise["name"].title(),
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"],
        } 
    }

headers={
    "Authorization": AUTH,
}

response=requests.post(sheety_endpoint,json=parameters,headers=headers)

