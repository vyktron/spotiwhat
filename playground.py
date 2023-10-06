from pymongo import MongoClient
import csv 

DB_NAME = 'local'
COLLECTION_NAME = 'spotify'

# header

# Remember to lauch mongo server before running this script
URI = "mongodb://root:admin@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

def mongoimport(csv_path, db_name, coll_name, connection_uri=URI) :
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documents in the new collection
    """
    mongoClient = MongoClient(connection_uri)
    db = mongoClient[db_name]
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

if __name__ == "__main__" :
    # path to csv file
    csv_path = 'db/spotify_db.csv'
    # name of mongo db
    db_name = 'local'
    # name of mongo db collection
    coll_name = 'spotify'
    print(mongoimport(csv_path, db_name, coll_name))