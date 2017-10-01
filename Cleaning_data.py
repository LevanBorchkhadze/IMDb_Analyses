import pandas
import csv

# creating new csv file without columns that won't be used
data = pandas.read_csv("movie_metadata.csv", encoding="ISO-8859-1")
drop_columns = data.drop(["color", "num_critic_for_reviews", "director_facebook_likes", "actor_3_facebook_likes",
                          "actor_1_facebook_likes", "cast_total_facebook_likes", "facenumber_in_poster", "plot_keywords",
                          "movie_imdb_link", "num_user_for_reviews", "language", "country", "content_rating",
                          "actor_2_facebook_likes", "aspect_ratio"], axis=1)

drop_columns.to_csv("clean_movie_data.csv")

with open('clean_movie_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    num_of_votes = []
    gross = []
    for row in reader:
        num_of_votes.append((float(row["num_voted_users"])))
        gross.append((float(row["gross"])))

# filtering movies with less than 8000 votes
num_of_votes_above_8000 = [index for index, value in enumerate(num_of_votes) if value < 8000]

# filtering movies with no gross revenue information
gross_clean_indexes = [index for index, value in enumerate(gross) if value <= 0 and index not in num_of_votes_above_8000]


total_indexes = num_of_votes_above_8000 + gross_clean_indexes

drop_rows_ratings = data.drop(total_indexes)
drop_rows_ratings.to_csv("clean_movie_data.csv")
