# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
""" only  Using for loop """
# for movie_id in movie_ids:
#     url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
#     response = requests.get(url)
#     data = response.json()
#     print(data["title"], "\n", data["overview"], "\n", data["vote_average"])

""" Use funtion to get movies data """
def movie_info(movie_ids):
    all_movies = []
    for movie_id in movie_ids:
        url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
        response = requests.get(url)
        data = response.json()
        all_movies.append(data)
    return all_movies

movies = movie_info(movie_ids)
for movie in movies:
    print(movie["title"], "\n", movie["overview"], "\n", movie["vote_average"])

# /YOUR CODE
