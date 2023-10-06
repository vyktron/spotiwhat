from pymongo import MongoClient
import csv 
import random

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
    mongoimport(csv_path, db_name, coll_name)

# function with the genre in input that returns the list of the songs of that genre
def get_songs(genre):
    mongoClient = MongoClient(URI)
    db = mongoClient[DB_NAME]
    collection = db[COLLECTION_NAME]
    songs = collection.find({"genre": genre})
    # convert the result to a list
    songs = list(songs)
    return songs

# function with a list of songs in input that return a shorter list of random songs with the sum of duration equal to the duration of wanted in hours
def get_playlist(songs, duration):
    # initialize the list
    playlist = []
    # initialize the sum of duration
    sum = 0
    # shuffle the list of songs
    random.shuffle(songs)
    # convert the duration from hours to milliseconds
    duration = int(duration * 3600000)
    # iterate over the list of songs
    for song in songs:
        # check if the sum of duration is less than 5 hours
        if sum < duration:
            # append the song to the playlist
            playlist.append(song)
            # update the sum of duration (convert the duration from string to int)
            sum += float(song["duration_ms"])
    return playlist

# call the function with the genre in input
songs = get_songs("pop")
playlist = get_playlist(songs, 5)
print(songs)