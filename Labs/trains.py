import requests
import csv
from bs4 import BeautifulSoup

# Irish Rail API link
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

# Get the webpage
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')
# To view raw XML uncomment below
# print(soup.prettify())

# All tags we want to pull data from
retrieveTags = ["TrainStatus",
                "TrainLatitude",
                "TrainLongitude",
                "TrainCode",
                "TrainDate",
                "PublicMessage",
                "Direction"
                ]

# Create CSV file to store data
with open("trains.csv", mode="w") as train_file:

    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Find train listings and print each one
    listings = soup.findAll("objTrainPositions")

    for listing in listings:
        # if you want to view the data, just print(listing) or for specific data, such as latitudes use print(listing.TrainLatitude.string) 

        # We only want trains south of Dublin, i.e. that have a latitude less than that of Dublin
        lat = float(listing.TrainLatitude.string)

        if lat < 53.4:

            # Create array to append each piece of data about train latitudes
            entryList = []

            # Loop through tags to append each to CSV file
            for tag in retrieveTags:
                entryList.append(listing.find(tag).string)
            
            # Write to CSV
            train_writer.writerow(entryList)