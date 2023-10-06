from pymongo import MongoClient
import csv 

DB_NAME = 'local'
COLLECTION_NAME = 'spotify'

# header

# Remember to lauch mongo server before running this script
URI = "mongodb://root:admin@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

def connection(uri=URI):
    """ Returns a connection to MongoDB
    """
    mongoClient = MongoClient(uri)
    return mongoClient


def mongoimport(csv_path, db_name, coll_name, client=connection()) :
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documents in the new collection
    """
    db = client[db_name]
    collection = db[coll_name]

    # Get the headers from the csv file
    header = []
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

    csvFile = open(csv_path, 'r')
    reader = csv.DictReader(csvFile)

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        collection.insert_one(row)
    
    return 1

# function with the genre in input that returns the list of the songs of that genre
def get_songs(genre, client):
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    songs = collection.find({"genre": genre})
    # convert the result to a list
    songs = list(songs)
    return songs

# call the function with the genre in input
songs = get_songs("pop")
print(songs)

if __name__ == "__main__" :
    # path to csv file
    csv_path = 'db/spotify_db.csv'
    # name of mongo db
    db_name = 'local'
    # name of mongo db collection
    coll_name = 'spotify'
    mongoimport(csv_path, db_name, coll_name)

