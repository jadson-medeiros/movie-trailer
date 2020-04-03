import json
import media

def get_movie_list(filepath):
    # filepath is a full file path to the json file.
    movielist = []
    with open(filepath) as jsonfile:
        jsondata = json.load(jsonfile)
        for key in jsondata:
            value = jsondata[key]
            moviecontent = media.Movie(value["title"],
                                       value["poster"],
                                       value["trailer"])
            moviecontent.update_from_json(value)
            movielist.append(moviecontent)
    # Return an array of movie information.
    return movielist
