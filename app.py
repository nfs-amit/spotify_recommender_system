import streamlit as st
import requests
from spotify_backend import recommend_songs   #✅ IMPORT THE RECOMMENDER FUNCTION

st.set_page_config(
    page_title="Spotify Recommender",
    page_icon="🎧",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #1DB954;
        }
        .card {
            background-color: #181818;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
        }
        .song-title {
            font-size: 20px;
            font-weight: bold;
        }
        .artist {
            color: #b3b3b3;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="title">🎧 Spotify Song Recommender</div>', unsafe_allow_html=True)
st.write("")

# INPUT
col1, col2 = st.columns([2, 1])

with col1:
    song_input = st.text_input("Enter Song or Artist Name")

with col2:
    mood = st.selectbox("Select Mood", ["None", "Happy", "Sad", "Chill", "Party"])
    genre = st.selectbox("Select Genre", ["None", "Pop", "Rock", "Hip-Hop", "Jazz", "EDM"])

# BUTTON
recommend_btn = st.button("🎵 Recommend Songs")


if recommend_btn:
    if song_input.strip() == "":
        st.error("⚠️ Please enter a song or artist name")
    else:
        with st.spinner("🔍 Finding recommendations..."):
            results = recommend_songs(song_input)   # ✅ CORRECT PLACE

        if not results:
            st.warning("No recommendations found 😢")
        else:
            st.subheader("✨ Recommended Songs")

            for song in results:
                st.markdown(f"""
                <div class="card">
                    <div style="display:flex; gap:15px;">
                        <div>
                            <div class="song-title">{song['song']}</div>
                            <div class="artist">🎤 {song['artist']}</div>
                            <div>🎼 Genre: {song['genre']}</div>
                            <div>🔥 Popularity: {song['popularity']}</div>
                            <a href="{song['url']}" target="_blank" style="color:#1DB954;">
                                ▶ Open in Spotify
                            </a>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# FOOTER
st.write("")
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ by Amit Kumar</center>",
    unsafe_allow_html=True
)