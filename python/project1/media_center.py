from media.media import Movie, Serie
from web import web

furious = Movie("Fast and Furious",
                "Sinopsis",
                "https://www.google.com.mx/imgres?imgurl=http%3A%2F%2Fcdn.bgr.com%2F2015%2F04%2Fthe_fast_and_the_furious_024-there-have-been-more-than-just-gear-changes-for-the-cast-of-the-fast-and-the-furious.jpeg&imgrefurl=http%3A%2F%2Fbgr.com%2F2015%2F04%2F29%2Ffast-and-furious-supercut-car-crashes%2F&docid=fYgcqM46C6SlvM&tbnid=A5gLatABr5p2aM%3A&w=1024&h=768&client=firefox-a&bih=740&biw=655&ved=0ahUKEwi9z5yl9_DMAhUUOVIKHdZxBkIQMwgzKAMwAw&iact=mrc&uact=8",
                "https://www.youtube.com/watch?v=ZsJz2TJAPjw",
                "93 min",
                "2001")

breaking_bad = Serie("Breaking Bad",
                     "Sinopsis",
                     "poster",
                     "trailer",
                     "5",
                     "AMC")

content = {"movies":[furious], "series":[breaking_bad]}

web.startSite(content)
