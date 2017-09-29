import csv
from collections import Counter
import numpy as np
import re
import matplotlib.pyplot as plt

actor_name_input = input("Please input name of the actor >")
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


actors_ratings = []
actors_gross = []
actors_budget = []
actors_movies = []
actors_director = []
actor_actors_1 = []
actor_actors_2 = []
actor_actors_3 = []
actors_director_indexes = []
director_ratings = []
actors_genres = []
genre_ratings = []
actors_genre_ratings = []


total_actors = actor_1_name + actor_2_name + actor_3_name


for i, (a1, a2, a3) in enumerate(zip(actor_1_name, actor_2_name, actor_3_name)):
    if a1 == actor_name_input or a2 == actor_name_input or a3 == actor_name_input:
        actors_ratings.append(imdb_rating[i])
        actors_budget.append(budget[i])
        actors_gross.append(gross[i])
        actors_movies.append((movie_title[i]))
        actors_director.append(directors[i])
        actors_genres.append(genres[i])


top_3_movies = sorted(zip(actors_ratings, actors_movies), reverse=True)[:3]

dc = Counter(actors_director)
top_3_directors = dc.most_common(3)

tot_actor_genres = [item for word in actors_genres for item in word.split('|')]
g = Counter(tot_actor_genres)
top_3_genre = g.most_common(3)

for i, (a1, a2, a3) in enumerate(zip(actor_1_name, actor_2_name, actor_3_name)):
    if (a1 == actor_name_input or a2 == actor_name_input or a3 == actor_name_input) and\
                    directors[i] == top_3_directors[0][0]:
        actors_director_indexes.append(i)

for i in actors_director_indexes:
    director_ratings.append(imdb_rating[i])

for i, v in enumerate(genres):
    if top_3_genre[0][0] in genres:
        genre_ratings.append(imdb_rating[i])

for i, v in enumerate(genres):
    if re.search(r'.*'+top_3_genre[0][0]+'.*', v) and \
                    actor_name_input == (actor_1_name[i] or actor_2_name[i] or actor_3_name[i]):
        actors_genre_ratings.append(imdb_rating[i])


print("Three most successful movies of", actor_name_input, "are:", "\n", top_3_movies[0][1], "-",
      top_3_movies[0][0], "\n",
      top_3_movies[1][1], "-", top_3_movies[1][0], "\n",
      top_3_movies[2][1], "-", top_3_movies[2][0])
print("Top three co-works:", top_3_directors[0][0], "-", top_3_directors[0][1], "|", top_3_directors[1][0], "-",
      top_3_directors[1][1], "|", top_3_directors[2][0], "-", top_3_directors[2][1])
print("Average movie rating for", actor_name_input, "and his most frequent director co-work", top_3_directors[0][0],
      "is:", round(np.mean(director_ratings), 2))
print("The average rating for", actor_name_input, "is", round(np.mean(actors_ratings), 2))
print("The average budget for", actor_name_input, "is", round(np.mean(actors_budget)))
print("The average gross revenue for", actor_name_input, "is", round(np.mean(actors_gross), 2))
print("The average profit for", round((np.mean(actors_gross) - np.mean(actors_budget)), 2))
print("Top 3 most frequent genres for", actor_name_input, "is:", "\n",
      top_3_genre[0][0], "-", top_3_genre[0][1], "|", top_3_genre[1][0],
      "-", top_3_genre[1][1], "|", top_3_genre[2][0], "-", top_3_genre[2][1])
print("Average", top_3_genre[0][0]," rating for whole database is", "-", round(np.mean(genre_ratings), 2), "\n",
      "Average", top_3_genre[0][0], " rating for", actor_name_input, "is -", round(np.mean(actors_genre_ratings), 2))


# plt.scatter(num_of_votes, gross)
# plt.scatter(num_of_votes, imdb_rating)
# plt.scatter(num_of_votes, budget)
# plt.scatter(imdb_rating, gross)
# plt.scatter(budget, gross)
# plt.show()

print("correlation between number of votes and gross revenue is:", round(np.corrcoef(num_of_votes, gross)[1][0], 2))
print("correlation between number of votes and imdb rating is:", round(np.corrcoef(num_of_votes, imdb_rating)[1][0], 2))
print("correlation between number of votes and budget is:", round(np.corrcoef(num_of_votes, budget)[1][0], 2))
print("correlation between imdb rating and gross revenue is:", round(np.corrcoef(imdb_rating, gross)[1][0], 2))
print("correlation between budget and gross revenue is:", round(np.corrcoef(budget, gross)[1][0], 2))

