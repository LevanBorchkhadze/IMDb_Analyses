import csv
from collections import Counter
import numpy as np

title = input("Please input movie title >")
with open('clean_movie_data.csv', 'r',) as f:
    reader = csv.DictReader(f)
    gross = []
    budget = []
    imdb_rating = []
    movie_title = []
    genres = []
    num_of_votes = []
    actor_1_name = []
    actor_2_name = []
    actor_3_name = []
    directors = []
    for row in reader:
        gross.append(float(row["gross"]))
        budget.append(float(row["budget"]))
        imdb_rating.append(float(row["imdb_score"]))
        movie_title.append(row["movie_title"])
        genres.append(row["genres"])
        num_of_votes.append((float(row["num_voted_users"])))
        actor_1_name.append(row["actor_1_name"])
        actor_2_name.append(row["actor_2_name"])
        actor_3_name.append(row["actor_3_name"])
        directors.append(row["director_name"])


c = Counter(directors)
# print(c["Gore Verbinski"])

director_ratings = []
director_gross = []
director_budget = []
director_total_actors = []
for i, x in enumerate(directors):
    if x == title:
        print(movie_title[i])
        print("Genres:", genres[i])
        print("Actors:", actor_1_name[i] + ",", actor_2_name[i] + ",", actor_3_name[i] + ".")

        director_ratings.append(imdb_rating[i])
        director_budget.append(budget[i])
        director_gross.append(gross[i])
        # director_total_actors.append(actor_1_name[i]  + ",", actor_2_name[i] + ",", actor_3_name[i] + ".")
        print("The average rating for", title, "is", round(np.mean(director_ratings)))
        print("The average budget for", title, "is", round(np.mean(director_budget)))
        print("The average gross revenue for", title, "is", round(np.mean(director_gross)))
        print("The average profit for", round(np.mean(director_gross)) - round(np.mean(director_budget)))
    else:
        print("Name of the director was not found in database")
        break

print(np.corrcoef(num_of_votes, gross)[1][0])
print(np.corrcoef(num_of_votes, imdb_rating)[1][0])
print(np.corrcoef(imdb_rating, gross)[1][0])
print(np.corrcoef(budget, gross)[1][0])
print(np.corrcoef(budget, num_of_votes)[1][0])
