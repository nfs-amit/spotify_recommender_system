import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("dataset.csv")

# Clean data
df = df.drop(columns=['Unnamed: 0'], errors='ignore')
df = df.dropna()
df = df.drop_duplicates(subset='track_id')

# -------------------------------
# FEATURE SELECTION
# -------------------------------
FEATURES = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo'
]

# -------------------------------
# NORMALIZATION
# -------------------------------
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[FEATURES] = scaler.fit_transform(df[FEATURES])

# Feature matrix
feature_matrix = df_scaled[FEATURES].values

# Reset index
df_scaled = df_scaled.reset_index(drop=True)

# -------------------------------
# RECOMMENDER FUNCTION
# -------------------------------
def recommend_songs(song_name, n=10):
    """
    Recommend songs based on similarity
    """

    # Exact match
    matches = df_scaled[df_scaled['track_name'].str.lower() == song_name.lower()]

    # Partial match if not found
    if matches.empty:
        matches = df_scaled[df_scaled['track_name'].str.lower().str.contains(song_name.lower())]

    # If still not found
    if matches.empty:
        return []

    idx = matches.index[0]

    # Compute similarity
    seed_vector = feature_matrix[idx].reshape(1, -1)
    similarities = cosine_similarity(seed_vector, feature_matrix)[0]

    # Get top similar songs
    similar_indices = similarities.argsort()[::-1][1:n+1]

    recommendations = df_scaled.iloc[similar_indices][[
        'track_name',
        'artists',
        'track_genre',
        'popularity'
    ]].copy()

    recommendations['similarity_score'] = similarities[similar_indices].round(4)

    # Convert to list of dictionaries (IMPORTANT for Streamlit)
    result = []
    for _, row in recommendations.iterrows():
        result.append({
            "song": row['track_name'],
            "artist": row['artists'],
            "genre": row['track_genre'],
            "popularity": int(row['popularity']),
            "similarity": float(row['similarity_score']),
            "url": f"https://open.spotify.com/search/{row['track_name'].replace(' ', '%20')}"
        })

    return result


# -------------------------------
# TEST (Optional)
# -------------------------------
if __name__ == "__main__":
    results = recommend_songs("Shape of You", 5)
    for r in results:
        print(r)