import csv
from collections import Counter
import numpy as np
import re
import matplotlib.pyplot as plt

director_name_input = input("Please input name of the director >")
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


director_ratings = []
director_gross = []
director_budget = []
director_movies = []
director_actor_1 = []
director_actor_1_indexes = []
director_actor_2 = []
director_actor_3 = []
actor_ratings = []
director_genres = []
genre_ratings = []
director_genre_ratings = []
for i, x in enumerate(directors):
    if x == director_name_input:
        director_ratings.append(imdb_rating[i])
        director_budget.append(budget[i])
        director_gross.append(gross[i])
        director_movies.append((movie_title[i]))
        director_actor_1.append(actor_1_name[i])
        director_actor_2.append(actor_2_name[i])
        director_actor_3.append(actor_3_name[i])
        director_genres.append(genres[i])


top_3_movies = sorted(zip(director_ratings, director_movies), reverse=True)[:3]
director_total_actors = director_actor_1 + director_actor_2 + director_actor_3

ac = Counter(director_total_actors)
top_3_actors = ac.most_common(3)

tot_direct_genres = [item for word in director_genres for item in word.split('|')]
g = Counter(tot_direct_genres)
top_3_genre = g.most_common(3)

for i, x in enumerate(directors):
    if x == director_name_input and actor_1_name[i] == top_3_actors[0][0]:
        director_actor_1_indexes.append(i)

for i in director_actor_1_indexes:
    actor_ratings.append(imdb_rating[i])

for i, v in enumerate(genres):
    if top_3_genre[0][0] in genres:
        genre_ratings.append(imdb_rating[i])

for i, v in enumerate(genres):
    if re.search(r'.*'+top_3_genre[0][0]+'.*', v) and director_name_input == directors[i]:
        director_genre_ratings.append(imdb_rating[i])


print("Three most successful movies of", director_name_input, "are:", "\n", top_3_movies[0][1], "-", top_3_movies[0][0], "\n",
      top_3_movies[1][1], "-", top_3_movies[1][0], "\n",
      top_3_movies[2][1], "-", top_3_movies[2][0])
print("Top three co-works:", top_3_actors[0][0], "-", top_3_actors[0][1], "|", top_3_actors[1][0], "-", top_3_actors[1][1], "|",
      top_3_actors[2][0], "-", top_3_actors[2][1])
print("Average movie rating for", director_name_input, "and his most frequent co-work", top_3_actors[0][0], "is:", round(np.mean(actor_ratings), 2))
print("The average rating for", director_name_input, "is", round(np.mean(director_ratings), 2))
print("The average budget for", director_name_input, "is", round(np.mean(director_budget)))
print("The average gross revenue for", director_name_input, "is", round(np.mean(director_gross), 2))
print("The average profit for", round((np.mean(director_gross) - np.mean(director_budget)), 2))
print("Top 3 most frequent genre for", director_name_input, "is:", "\n",
      top_3_genre[0][0], "-", top_3_genre[0][1], "|", top_3_genre[1][0],
      "-", top_3_genre[1][1], "|", top_3_genre[2][0], "-", top_3_genre[2][1])
print("Average", top_3_genre[0][0]," rating for whole database is", "-", round(np.mean(genre_ratings), 2), "\n",
      "Average", top_3_genre[0][0], " rating for", director_name_input, "is -", round(np.mean(director_genre_ratings)), 2)


plt.scatter(num_of_votes, gross)
plt.scatter(num_of_votes, imdb_rating)
plt.scatter(num_of_votes, budget)
plt.scatter(imdb_rating, gross)
plt.scatter(budget, gross)

# print(round(np.corrcoef(num_of_votes, gross)[1][0], 2))
# print(round(np.corrcoef(num_of_votes, imdb_rating)[1][0], 2))
# print(round(np.corrcoef(num_of_votes, budget)[1][0], 2))
# print(round(np.corrcoef(imdb_rating, gross)[1][0], 2))
# print(round(np.corrcoef(budget, gross)[1][0], 2))
