from pymongo import MongoClient
import csv 
import random
import src


DB_NAME = 'local'
COLL_NAME = 'spotify'
CSV_PATH = src.DB + '/spotify_db.csv'

# header

# Remember to lauch mongo server before running this script
URI = "mongodb://root:admin@localhost:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

# Function that returns a connection to MongoDB
def connection(uri=URI):
    """ Returns a connection to MongoDB
    """
    mongoClient = MongoClient(uri)
    return mongoClient

# Function that imports a csv file to a mongo collection
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

# Function that returns the list of the genres (the "nb" most popular ones)
# That contains the "base_genre" in their name
def get_genres(base_genre, db_name, coll_name, client=connection(), nb=10):
    db = client[db_name]
    collection = db[coll_name]
    genres = collection.find({"genre": {"$regex": base_genre}}).distinct("genre")
    # Get the "nb" most popular genres
    genres = sorted(genres, key=lambda x: -collection.count_documents({"genre": x}))
    # convert the result to a list
    genres = list(genres)
    return genres[:nb]

# Function that takes the a list of genres in input and returns a list of songs that have one of the genres in their genre
def get_songs(genre : list, db_name : str, coll_name :str, client = connection()):
    db = client[db_name]
    collection = db[coll_name]
    songs = []
    for g in genre:
        songs += list(collection.find({"genre": g}))
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

def get_playlist_from_genre(genre, duration, db_name, coll_name):
    genre_list = get_genres(genre, db_name, coll_name)
    songs = get_songs(genre_list, db_name, coll_name)
    playlist = get_playlist(songs, duration)
    return playlist

# Function to prepare the data for the front end
# It returns a preview of the playlist with the name of the songs and the artists (nb songs)
# and the average danceability of the playlist
def front_infos(playlist, nb=10):
    infos = []
    danceability = 0

    for song in playlist:
        # Get the name of the songs and the artists
        if len(infos) < nb:
            infos.append(song["trackName"] + " - " + song["artistName"])
        # Get the average danceability
        danceability += float(song["danceability"])

    # return the playlist
    return infos, danceability, len(playlist)

if __name__ == "__main__" :
    # path to csv file
    csv_path = 'db/spotify_db.csv'
    # name of mongo db
    db_name = 'local'
    # name of mongo db collection
    coll_name = 'spotify'

    genre_list = get_genres("country")
    songs = get_songs(genre_list)
    playlist = get_playlist(songs, 5)
    infos, danceability, length = front_infos(playlist)
    print(infos)


