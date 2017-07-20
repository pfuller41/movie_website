import fresh_tomatoes
import media

apocalypse_now = media.Movie("Apocalypse Now", "https://i.ytimg.com/vi_webp/FAlARcNhQ3A/movieposter.webp", "https://www.youtube.com/watch?v=FAlARcNhQ3A", "1979")
raging_bull = media.Movie("Raging Bull","https://i.ytimg.com/vi_webp/8_tETBw4dNg/movieposter.webp", "https://www.youtube.com/watch?v=8_tETBw4dNg", "1980")
deer_hunter = media.Movie("Deer Hunter", "https://i.ytimg.com/vi_webp/3aED2kxM2qM/movieposter.webp", "https://www.youtube.com/watch?v=3aED2kxM2qM", "1979")
silence_of_the_lambs = media.Movie("The Silence of the Lambs", "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg", "https://www.youtube.com/watch?v=Lr3OavheNu0", "1991")
the_godfather = media.Movie("The Godfather", "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", "https://www.youtube.com/watch?v=dNE2PvbesQU", "1972")
a_clockwork_orange = media.Movie("A Clockwork Orange", "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Clockwork_orangeA.jpg/220px-Clockwork_orangeA.jpg","https://www.youtube.com/watch?v=9JIc_1v7i88", "1972")
movies = [apocalypse_now, deer_hunter, raging_bull, the_silence_of_the_lambs, the_godfather, a_clockwork_orange]
fresh_tomatoes.open_movies_page(movies)