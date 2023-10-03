import requests
from datetime import datetime

USERNAME = 'username'
TOKEN = 'token'
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': graph_id,
    'name': 'Learning',
    'unit': 'Min',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixels_endpoint = f"{graph_endpoint}/{graph_id}"
today = datetime.today()
new_today = today.strftime("%Y%m%d")
print(new_today)

pixel_config = {
    'date': new_today,
    'quantity': input("How many minutes did you study today? ")
}

response = requests.post(url=pixels_endpoint, json=pixel_config, headers=headers)
print(response.text)

put_endpoint = f"{pixels_endpoint}/{new_today}"

put_params = {
    'quantity': '55'
}
# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

del_endpoint = put_endpoint

# response = requests.delete(url=del_endpoint, headers=headers)
# print(response.text)
