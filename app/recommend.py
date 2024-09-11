import pickle
from fetch_poster import fetch_poster


movies = pickle.load(open('../new_df.pkl', 'rb'))
similarity = pickle.load(open('../similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True , key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
         movie_id = movies.iloc[i[0]].movie_id
         
         recommended_movies.append(movies.iloc[i[0]].title)
         # fetch poster of api
         recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters     