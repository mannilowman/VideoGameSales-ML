import streamlit as st
import pickle
import pandas as pd

# Ladda modellen och encoders
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/le_platform.pkl', 'rb') as f:
    le_platform = pickle.load(f)

with open('models/le_genre.pkl', 'rb') as f:
    le_genre = pickle.load(f)

st.title("🎮 Video Game Sales Predictor")
st.write("Förutsäg global försäljning baserat på plattform, genre och år.")

platform = st.selectbox("Plattform", le_platform.classes_)
genre = st.selectbox("Genre", le_genre.classes_)
year = st.number_input("År", min_value=1980, max_value=2025, value=2020)

if st.button("Förutsäg försäljning"):
    platform_encoded = le_platform.transform([platform])[0]
    genre_encoded = le_genre.transform([genre])[0]

    input_data = pd.DataFrame([[platform_encoded, genre_encoded, year]],
                                columns=['Platform_encoded', 'Genre_encoded', 'Year'])

    prediction = model.predict(input_data)[0]
    st.success(f"Förutspådd global försäljning: **{prediction:.2f} miljoner exemplar**")