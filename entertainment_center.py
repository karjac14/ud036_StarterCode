import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "G",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", "1995", "Fantasy/Adventure")
pearl_harbor = media.Movie("Pearl Harbor",
                        "PG-7",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/pearl-harbor-2001/large_tt7SGLAp4Du2PqxaFVNrHNLob9s.jpg",
                        "https://www.youtube.com/watch?v=yzK0GBEkFxc", "2001", "Drama film/Action")
finding_nemo = media.Movie("Finding Nemo",
                        "G",
                        "http://www.goldenglobes.com/sites/default/files/styles/portrait_medium/public/films/finding_nemo.jpeg?itok=grIy9dHa&c=bce87a9e2fc72060ed86405504fbb373",
                        "https://www.youtube.com/watch?v=wZdpNglLbt8", "2003", "Fantasy/Adventure")
the_last_samurai = media.Movie("The Last Samurai",
                        "R",
                        "http://www.gstatic.com/tv/thumb/movieposters/33171/p33171_p_v8_aj.jpg",
                        "https://www.youtube.com/watch?v=T50_qHEOahQ", "2003", "Drama film/Action")
kingdom_of_heaven = media.Movie("Kingdom of Heaven",
                        "PG",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcRi6Gza7H2yzrOMgGITTjbt_A3GtsAmUyCDP2ut59MvZBUhjuzd",
                        "https://www.youtube.com/watch?v=-oO6pCRe3pM", "2005", "Drama film/Action")
the_shack = media.Movie("The Shack",
                        "PG-7",
                        "https://i.ytimg.com/vi/VZwpQ3CZ7Ck/movieposter.jpg",
                        "https://www.youtube.com/watch?v=CL0yUbSS5Eg", "1997", " Fantasy/Drama film")

stranger_things = media.Tv("Stranger Things",
                        "PG-7",
                        "http://static.rogerebert.com/redactor_assets/pictures/5786d08996d833f89c000039/stranger_things_poster.jpg",
                        "https://www.youtube.com/watch?v=vgS2L7WPIO4", "2", "Netflix")


movies = [the_last_samurai, stranger_things, the_shack, finding_nemo,
          kingdom_of_heaven, pearl_harbor, toy_story]

fresh_tomatoes.open_movies_page(movies)
