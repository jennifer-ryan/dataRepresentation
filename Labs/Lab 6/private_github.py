import requests, json


apiKey = "35e9a5515609f54347523d7eb0ce9c60ec1da4b4"

url = "https://api.github.com/repos/me50/jennifer-ryan"

response = requests.get(url, auth=("token", apiKey))

repoJSON = response.json()

#print(repoJSON)

filename = "private_github.json"

file = open(filename, "w")
json.dump(repoJSON, file, indent=4)
