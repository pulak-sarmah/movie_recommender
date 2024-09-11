import streamlit as st
import pickle
from recommend import recommend

# Load movies data
movies = pickle.load(open('../new_df.pkl', 'rb'))

# Movie list for the selectbox
movies_list = movies['title'].values

# Title of the app
st.title('🎬 Movie Recommender System')

# Selectbox for movie selection
selected_movie_name = st.selectbox(
    'Which movie do you like?', 
    movies_list,
    placeholder="Choose an option",
    label_visibility="visible"
)

# Button to trigger recommendations
if st.button('Recommend'):
    st.write('You selected:', selected_movie_name)

    # Show loader while fetching the recommendations
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie_name)
    
    # Display recommendations
    st.subheader('Here are some recommendations for you:')

    # Define layout with 5 columns for displaying recommendations
    col1, col2, col3, col4, col5 = st.columns(5)

    # Movie 1
    with col1:
        st.image(posters[0], width=100)
        st.caption(names[0])  # caption to prevent scrolling
    
    # Movie 2
    with col2:
        st.image(posters[1], width=100)
        st.caption(names[1])

    # Movie 3
    with col3:
        st.image(posters[2], width=100)
        st.caption(names[2])

    # Movie 4
    with col4:
        st.image(posters[3], width=100)
        st.caption(names[3])

    # Movie 5
    with col5:
        st.image(posters[4], width=100)
        st.caption(names[4])

# Additional styling for UI improvements
st.markdown("""
    <style>
    /* Styling the selectbox */
    div[data-baseweb="select"] > div {
        border: 1px solid #00b4d8;
        border-radius: 10px;
    }
    /* Styling the title */
    .stApp h1 {
        color: #0077b6;
        text-align: center;
        margin-bottom: 40px;
    }
    /* Styling the movie posters and captions */
    .stApp img {
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .stApp .stCaption {
        text-align: center;
        color: #023e8a;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
