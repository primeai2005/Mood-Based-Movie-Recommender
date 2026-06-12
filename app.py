import streamlit as st
import requests
import random
from movies import movies

API_KEY = "98d1aedc"

def fetch_poster(movie_name):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}"
    
    response = requests.get(url)
    data = response.json()

    print(data)  # 👈 keep this for debugging

    if data.get("Response") == "True":
        poster = data.get("Poster")
        
        if poster and poster != "N/A":
            return poster
    
    return None

st.title("🎬 Mood-Based Movie Recommender")

mood = st.selectbox("Choose your mood:", list(movies.keys()))

if st.button("Recommend"):
    st.subheader("🎥 Movies for you:")

    recommendations = random.sample(movies[mood], min(3, len(movies[mood])))

    cols = st.columns(len(recommendations))

    for i, movie in enumerate(recommendations):
        poster = fetch_poster(movie)
        
        with cols[i]:
            st.text(movie)
            if poster:
                st.image(poster)