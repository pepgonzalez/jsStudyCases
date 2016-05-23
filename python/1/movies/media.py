#primera clase
import webbrowser

#google python Sytle Guide -> como debes escribir codigo
class Movie():
    def __init__(self, title, storyline, url, poster):
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = url
        self.poster_image_url = poster

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
        
