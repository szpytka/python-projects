# https://pixe.la/v1/users/jszpytka/graphs/cycling.html
import requests
import datetime as dt

USERNAME = "------" #username to create
TOKEN = "-----------" #token to give
GRAPH_ID = "-----------" #id of the graph

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Habit Tracker", #example graph
    "unit": "Km", #example unit
    "type": "float", #example type (int/float)
    "color": "ichou" #example color from documentation
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

today = str(dt.datetime.now().strftime("%Y%m%d"))
quantity = input("How many Km: ")
today_year = dt.datetime.now().strftime("%Y")
today_month = dt.datetime.now().strftime("%m")
today_day = dt.datetime.now().strftime("%d")
print(f"{today_day}/{today_month}/{today_year}")

pixel_data = {
    "date": today,
    "quantity": quantity,
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# CREATE USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# CREATE FUNCTIONALITY
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text[12:20])
