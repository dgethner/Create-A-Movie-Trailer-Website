#We have to import or bring in the module webbrowser to be able to
#have a window open in a webbrowser in the show_trailer function. 
import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director, launch_date, duration, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.launch_date = launch_date
        self.duration = duration
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
