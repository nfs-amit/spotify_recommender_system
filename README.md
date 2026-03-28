# 🎧 Spotify Song Recommender System

A modern and interactive web application that recommends songs based on user input using machine learning and a clean Streamlit interface.

## 🚀 Project Overview

This project is a **Spotify Song Recommender System** that suggests similar songs based on audio features such as danceability, energy, tempo, and more.

The project is divided into two parts:

* 📊 **Data Analysis & Model Building** using Jupyter Notebook (`spotify.ipynb`)
* 🌐 **Frontend Application** using Streamlit (`app.py`)
## 🔗 GitHub Repository

👉 https://github.com/nfs-amit/spotify_recommender_system.git

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Data Analysis:** Jupyter Notebook
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Algorithm:** Cosine Similarity
* **IDE:** VS Code

## ✨ Features

* 🎵 Enter song or artist name
* 🔍 Get top recommended songs
* 📊 Based on audio feature similarity
* 🌙 Dark-themed UI (Spotify style)
* 🔗 Clickable Spotify links
* 📈 Data analysis and visualization included

## 📁 Project Structure

```bash
spotify-project/
│
├── app.py                    # Streamlit frontend
├── spotify_backend.py        # Recommendation logic
├── spotify.ipynb             # EDA + analysis + model building
├── dataset.csv               # Dataset
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
```


## 📊 About `spotify.ipynb`

This notebook includes:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* Data visualization (plots, graphs)
* Similarity model building
--
## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nfs-amit/spotify_recommender_system.git
cd spotify_recommender_system
```

### 2️⃣ Create virtual environment (optional)

```bash
python -m venv env
env\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🌐 How to Use

1. Enter a song or artist name
2. Click on **"Recommend Songs"**
3. View recommended songs with details
4. Click to open songs in Spotify

---

## 📸 Application Screenshot

![Spotify Recommender UI](screenshot.png)

---

## 🧠 How It Works

* Audio features are extracted from dataset
* Data is normalized using MinMaxScaler
* Cosine Similarity is used to find similar songs
* Top recommendations are displayed

---

## 🚀 Future Improvements

* 🎵 Spotify API integration
* 🖼️ Album cover images
* ▶️ Audio preview feature
* 🔍 Auto-suggestions
* 🌐 Deployment (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Amit Kumar**
Aspiring Data Analyst 

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
