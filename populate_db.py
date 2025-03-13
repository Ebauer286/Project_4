from pymongo import MongoClient
import csv
from pathlib import Path

client = MongoClient(port = 27017)
db = client['proj_4']
collection = db['mushrooms']


if collection.count_documents({}) != 0:
    print("Mushroom dataset is already entered into database.")
else:
    path = Path('MushroomDataset/secondary_data.csv')
    data = []
    with open(path, 'r+') as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)

        for row in reader:
            d = dict(zip(headers, row))
            data.append(d)

    collection.insert_many(data)

