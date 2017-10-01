# IMDb_analyses

## Summary
The project consists of three modules: 1.movie comparison 2.director infos 3.actor infos. Source of the data is kaggle [IMDB 5000 Movie Dataset](https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset/data) project. 

## Descreption of Modules
### General Calcuations
Along with specific modules, the application will also give general information about:
1. correlation between number of votes and gross revenue
2. correlation between number of votes and gross imdb rating
3. correlation between number of votes and budget revenue
4. correlation between imdb rating and gross revenue
5. correlation between budget and gross revenue

### Movie comparison (under constrauction)
The module gives user opportunity to compare up to 3 movies. User inputs the movie title, if the title exists in database it gives following processed information:
1. Movie title
2. Name of director
3. Names of 3 stars
4. Movie genre/genres
5. IMDb rating
6. Average genre rating
7. Average release year rating
8. Average movie rating for 1st actor
9. Average movie rating for the director
10. Budget
11. Average genre Budget
12. Gross
13. Average genre gross
14. Profit
15. Average genre profit

## Director info
Based on inputed director name (if exists in database), the module gives following information:
1. Three most successful movies
2. Top three co-works
3. Average movie rating with its most frequent actor co-work
4. The average rating for the director
5. The average budget for the director
6. The average gross revenue for the director
7. The average profit for for the director
8. Top 3 most frequent genres for the director

## Actor info
Based on inputed actor name (if exists in database), the module gives following information:
1. Three most successful movies
2. Top three co-works
3. Average movie rating with its most frequent director co-work
4. The average rating for the actor
5. The average budget for the actor
6. The average gross revenue for the actor
7. The average profit for for the actor
8. Top 3 most frequent genres for the actor

## Celaning the data
According to calculations made, correlation between movie rating and gross/profit increses as the number of voters increse. 
Based on the result we assume that we should work only with movies with at least 7,000 votes. There are lots of rows with no gross information, and it was also cleaned. As a result we have about 3,500 rows instead of initial 5,000. Data aslo consists lots of rows that we're not going to use, which means that we also deleted following columns: color, num_critic_for_reviews, director_facebook_likes,  actor_3_facebook_likes, actor_1_facebook_likes, cast_total_facebook_likes, facenumber_in_poster, plot_keywords, movie_imdb_link, num_user_for_reviews, language, country, content_rating, actor_2_facebook_likes, aspect_ratio.
