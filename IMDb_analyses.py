import csv
import numpy
import matplotlib.pyplot as plt

with open('movie_metadata.csv', 'r', encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    gross = []
    budget = []
    imdb_rating = []
    movie_title = []
    revenue = []
    for row in reader:
        gross.append(float(row["gross"]))
        budget.append(float(row["budget"]))
        imdb_rating.append(float(row["imdb_score"]))
        movie_title.append(row["movie_title"])
        revenue.append(budget + gross)


gross_clean_indexes = [index for index, value in enumerate(gross) if value > 50]

gross_clean = []
ratings_clean = []
budget_clean = []

for index in gross_clean_indexes:
    gross_clean.append(gross[index])
for index in gross_clean_indexes:
    ratings_clean.append(imdb_rating[index])
for index in gross_clean_indexes:
    budget_clean.append(budget[index])

print(numpy.corrcoef(ratings_clean, gross_clean))
print(numpy.corrcoef(ratings_clean, budget_clean))
print(numpy.corrcoef(budget_clean, gross_clean))

plt.scatter(budget_clean, gross_clean)
plt.show()

