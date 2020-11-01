import requests

#url = 'https://gmit.ie'
#response = requests.get(url)
#print(response.headers)

url = 'http://127.0.0.1:5000/cars'

# pulling data from cars
response = requests.get(url)
d = response.json()

for car in d["cars"]:
    print (car)


# dict object below will get utomatically converted to json by the requests package
data = {
    "reg":"123", 
    "make":"toyota",
    "model":"auris",
    "price":12000
}

# posting the above to cars server
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

# updating a car in the server

dataString = {
    "make": "Ford",
    "model": "Kuga" 
}

car_url = "http://127.0.0.1:5000/cars/test"

response = requests.put(car_url, json=dataString)

print(response.status_code)
print(response.text)

# delete a car
url = 'http://127.0.0.1:5000/cars/123'

response = requests.delete(url)
print(response.status_code)
print(response.text)