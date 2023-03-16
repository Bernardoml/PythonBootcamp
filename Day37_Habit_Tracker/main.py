import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Creating the username using the POST method
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph definition using the POST method
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

# Setting the header needed to authenticate
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_params = {
    "id": "study-graph",
    "name": "Study Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

## Get the graph created - /v1/users/<username>/graphs/<graphID>
# graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}"
# response = requests.get(url=create_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

## Post a pixel using the POST method
post_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}"

# Getting today and formatting as yyyymmdd
# %Y - Year, full version - 2022
# %m - Month as a number 01-12 - 03
# %d - Day as a number 01-31 - 16
today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

# Using an input method to ask how many minutes you did study, to then post on the api
pixel_params = {
    "date": today_formatted,
    "quantity": input("How many minutes did you study today? "),
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


## Updating a pixel with PUT method
update_date = "20220315"
update_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}/{update_date}"

update_pixel_params = {
    "quantity": "0",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)


## Deleting a pixel with DELETE method
delete_date = "20220315"
delete_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}/{delete_date}"

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)


