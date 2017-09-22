import csv


with open('movie_metadata.csv', 'r', encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        gross = row["gross"]
        budget = row["budget"]
        imdb_rating = row["imdb_score"]
        print(imdb_rating)
