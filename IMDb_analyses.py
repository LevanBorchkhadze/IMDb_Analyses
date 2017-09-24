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

imdb_rating_clean = [i for i in imdb_rating if i > 0]
print(len(imdb_rating_clean))
gross_clean = [i for i in gross if i > 0]
print(len(gross_clean))
budget_clean = [i for i in budget if i > 0]
print(len(revenue))

print(numpy.corrcoef(imdb_rating, budget))
plt.scatter(imdb_rating, budget)
plt.show()