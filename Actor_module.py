import csv
from collections import Counter
import numpy as np
import re

# input value (actor name)
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
    durations = []
    # creating separate lists for each column of the csv file
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
        durations.append(row["durations"])

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

# creating new lists with indexes of specific columns in order to get corresponding information
# about values of different columns
for i, (a1, a2, a3) in enumerate(zip(actor_1_name, actor_2_name, actor_3_name)):
    if a1 == actor_name_input or a2 == actor_name_input or a3 == actor_name_input:
        actors_ratings.append(imdb_rating[i])
        actors_budget.append(budget[i])
        actors_gross.append(gross[i])
        actors_movies.append((movie_title[i]))
        actors_director.append(directors[i])
        actors_genres.append(genres[i])

# list of top 3 movies of the input actor name ordered by imdb_rating
top_3_movies = sorted(zip(actors_ratings, actors_movies), reverse=True)[:3]

# getting 3 most common directors from list created above for the input director name
dc = Counter(actors_director)
top_3_directors = dc.most_common(3)

# list of total genres for the input actor name
tot_actor_genres = [item for word in actors_genres for item in word.split('|')]

# getting 3 most common genres from list created above for the input actor name
g = Counter(tot_actor_genres)
top_3_genre = g.most_common(3)

# getting indexes of co-works between input actor name and most common director
for i, (a1, a2, a3) in enumerate(zip(actor_1_name, actor_2_name, actor_3_name)):
    if (a1 == actor_name_input or a2 == actor_name_input or a3 == actor_name_input) and\
                    directors[i] == top_3_directors[0][0]:
        actors_director_indexes.append(i)

# getting imdb_ratings for input actor name and its most common actor
for i in actors_director_indexes:
    director_ratings.append(imdb_rating[i])

# getting imdb_ratings for input actor most common genre from whole database
for i, v in enumerate(genres):
    if top_3_genre[0][0] in genres:
        genre_ratings.append(imdb_rating[i])

# getting imdb_ratings for input actor most common genre
for i, v in enumerate(genres):
    if re.search(r'.*'+top_3_genre[0][0]+'.*', v) and \
                    actor_name_input == (actor_1_name[i] or actor_2_name[i] or actor_3_name[i]):
        actors_genre_ratings.append(imdb_rating[i])

# printing specific results corresponding to input director name
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

# printing general information about whole database
print("correlation between number of votes and gross revenue is:", round(np.corrcoef(num_of_votes, gross)[1][0], 2))
print("correlation between number of votes and imdb rating is:", round(np.corrcoef(num_of_votes, imdb_rating)[1][0], 2))
print("correlation between number of votes and budget is:", round(np.corrcoef(num_of_votes, budget)[1][0], 2))
print("correlation between imdb rating and gross revenue is:", round(np.corrcoef(imdb_rating, gross)[1][0], 2))
print("correlation between budget and gross revenue is:", round(np.corrcoef(budget, gross)[1][0], 2))
print("correlation between budget and gross revenue is:", round(np.corrcoef(durations, imdb_rating)[1][0], 2))
print("correlation between budget and gross revenue is:", round(np.corrcoef(durations, gross)[1][0], 2))
