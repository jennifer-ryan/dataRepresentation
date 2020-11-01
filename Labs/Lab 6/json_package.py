import json

# dict object below
data = {
    "name":"joe",
    "age":21,
    "student":True    
}

#convert to json
file = open("simple.json", "w")
#json.dump(data, file, indent=4) #indent makes it neat

#dumps just turns it to a string
jsonString = json.dumps(data)
print(jsonString)
