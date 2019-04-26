import pickle

# Define some variables that will be put into pickle

Album = ( "Rammstain",
          "Mutter",
          1991,
          ( (1, "Mutter"),
            (2, "Moskau"),
            (3, "Herzlich")))

var_num = 14356
var_str = "Test string to pickle"


with open("vars.pickle", "wb") as vars_pickled:
    pickle.dump(Album, vars_pickled)
    pickle.dump(var_num, vars_pickled)
    pickle.dump(var_str, vars_pickled)

with open("vars.pickle", "rb") as vars_pickled:
    Album_loaded = pickle.load(vars_pickled)
    var_num_loaded = pickle.load(vars_pickled)
    var_str_loaded = pickle.load(vars_pickled)

    artist, album_title, year, tracks = Album_loaded
    print(artist)
    print(album_title)
    print(year)
    for track in tracks:
        track_num, title = track
        print("Track {0} has title {1}".format(track_num, title))