from github import Github
import requests

g = Github("35e9a5515609f54347523d7eb0ce9c60ec1da4b4")

# Prints user and repositories in my github
#for repo in g.get_user().get_repos(): 
#    print(repo.name)

repo = g.get_repo("jennifer-ryan/dataRepresentation")
#print(repo.clone_url)

fileInfo = repo.get_contents("exercise1.xml")
urlOfFile = fileInfo.download_url

#print(urlOfFile)

# prints contents of the xml file in the repository
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)