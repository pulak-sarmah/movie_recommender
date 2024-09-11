import requests
import os
from dotenv import load_dotenv
 


def fetch_poster(movie_id):
    load_dotenv()
    # Retrieve the API key from the .env file
    api_key = os.getenv("API_KEY")

    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+ data["poster_path"]
    
  
  
  