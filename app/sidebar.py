import streamlit as st

def render_sidebar(cities, room_types, seasons):
    st.sidebar.image("assets/logo.png", width=150)
    st.sidebar.header("Paramètres")

    city = st.sidebar.selectbox("Ville", options=cities)
    room_type = st.sidebar.selectbox("Type de logement", options=room_types)
    season = st.sidebar.selectbox("Saison", options=seasons)
    minimum_nights = st.sidebar.slider("Nombre de nuits minimum", 1, 15, 1)
    num_people = st.sidebar.slider("Nombre de personnes", 1, 5, 1)

    submit = st.sidebar.button("Prédire le prix")

    return {
        "city": city,
        "room_type": room_type,
        "season": season,
        "minimum_nights": minimum_nights,
        "num_people": num_people,
        "submit": submit
    }
