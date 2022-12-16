import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

respond = requests.get("https://opentdb.com/api.php", params=parameters)
respond.raise_for_status()
question_data = respond.json()["results"]
