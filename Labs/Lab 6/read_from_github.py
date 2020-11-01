import requests, json
from xlwt import *


# url = "https://api.github.com/users?since=100" 
url = "https://api.github.com/users/andrewbeattycourseware/followers" 

response = requests.get(url) 

data = response.json() 

#print(data) 

# write data to json file 
filename = 'githubusers.json' 

with open(filename, 'w') as f: 
    json.dump(data, f, indent=4)

# write data to excel file

# create workbook
w = Workbook()

# create sheet
ws = w.add_sheet("followers")
row = 0

#add headings
ws.write(row,0,"user login")
ws.write(row,1,"user repo")
row += 1

#add each car
for d in data:
    ws.write(row,0,d["login"])
    ws.write(row,1,d["url"])
    row +=1

w.save("followers.xls")    