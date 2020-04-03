# Movie is a class.
class Movie(object):
    # Definition fo a movie card.
    title = ""
    poster_image_url = ""
    trailer_youtube_url = ""
    storyline = ""
    year = ""
    
    def __init__(self, title, poster, trailer):
        # Constructor.
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def update_from_json(self, movieinfo):
        # This method fills the object
        # with the information that is in a json file.
        self.title = movieinfo["title"]
        self.poster_image_url = movieinfo["poster"]
        self.trailer_youtube_url = movieinfo["trailer"]
        self.storyline = movieinfo["storyline"]
        self.year = movieinfo["year"]
        
    # This method is separete to update a storyline.
    def update_storyline(self, storyline):
        
        self.storyline = storyline
