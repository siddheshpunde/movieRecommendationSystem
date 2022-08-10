import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommended(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    lst_1=[]
    lst_2=[]
    for i in distances:
        lst_1.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        lst_2.append(fetch_poster(movie_id))
    return lst_1,lst_2


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox("Type or select a movie from the dropdown",movies['title'].values)
if st.button('Recommend'):
    recommended_movie,recommended_posters=recommended(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_posters[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_posters[4])

