import requests
from datetime import datetime

USERNAME = "Your Name"
TOKEN = "Your Key"
GRAPH_ID = "graph1"

today = datetime.now()

# Create User In Pixela Website
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",  
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create Graph In Pixela Profile
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Learning Hours",
    "unit" : "Hour",
    "type" : "float",
    "color" : "momiji"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Create Pixel In Graph 
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "2.5",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Edit Graph In Pixela Profile
edit_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

edit_graph_config = {
    "timezone" : "Africa/Cairo"
}

response = requests.put(url=edit_graph_endpoint, json=edit_graph_config, headers=headers)
print(response.text)

# Delete Graph In Pixela Profile
delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.delete(url=delete_graph_endpoint, headers=headers)
print(response.text)

