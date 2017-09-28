import csv
import numpy
import matplotlib.pyplot as plt

with open('clean_movie_data.csv', 'r') as f:
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
    director = []
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
        director.append(row["director_name"])
gross_clean_indexes = [index for index, value in enumerate(gross) if value > 0]
num_of_votes_above_8000 = [index for index, value in enumerate(num_of_votes) if value < 8000]


print(gross_clean_indexes)
print(num_of_votes_above_8000)
gross_clean = []
ratings_clean = []
budget_clean = []


for index in gross_clean_indexes:
    gross_clean.append(gross[index])
for index in gross_clean_indexes:
    ratings_clean.append(imdb_rating[index])
for index in gross_clean_indexes:
    budget_clean.append(budget[index])

gross_clean = numpy.array(gross_clean)
ratings_clean = numpy.array(ratings_clean)
budget_clean = numpy.array(budget_clean)
profit = (gross_clean - budget_clean)

# print(numpy.corrcoef(ratings_clean, gross_clean)[1][0])
# print(numpy.corrcoef(ratings_clean, budget_clean)[1][0])
# print(numpy.corrcoef(budget_clean, gross_clean)[1][0])
# print(numpy.corrcoef(ratings_clean, profit)[1][0])
# plt.scatter(ratings_clean, profit)
# plt.show()

# num_of_votes_above_10000 = []
#
# num_of_votes_above_10000 = [num_of_votes_above_10000.append for r in num_of_votes if r > 10000]


# print(len(num_of_votes_above_10000))
# print(imdb_rating[enumerate(movie_title["Quantum of Solace"])])
# print(enumerate(movie_title["Quantum of Solace"]))


# imdb_rating_asd = [title for title, value in enumerate(movie_title) if value == "Quantum of Solace "]
# imdb_rating_index =int(imdb_rating_asd)
# print(imdb_rating_asd)
# print(imdb_rating[imdb_rating_asd])

# for genre in genres:
# print(genre)