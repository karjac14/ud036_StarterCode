class Video():
    def __init__(self, title, rating, image_url, trailer_url):
        """Inits video objects.

        Constructs and a method for opening trailer in a webbrowser.

        Attributes:
            all attributes are self explanatory unless described below,
            rating: ratings such as G, PG, PG-13, R, F , S
            trailer_url: youtube video url in string
        """
        self.title = title
        self.rating = rating
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    def __init__(self, title, rating, image_url, trailer_url, year, genre):
        """Inits movie objects and other attrs."""
        Video.__init__(self, title, rating, image_url, trailer_url)
        self.year = year
        self.genre = genre


class Tv(Video):
    def __init__(self, title, rating, image_url, trailer_url, season, network):
        """Inits TV objects and other attrs."""
        Video.__init__(self, title, rating, image_url, trailer_url)
        self.season = season
        self.network = network
