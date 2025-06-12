import pandas as pd
import pickle

# Charger le modèle
with open("../model/airbnb_price.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(inputs):
    cities, room_types, seasons = inputs["city"], inputs["room_type"], inputs["season"]

    # Convertir les entrées utilisateur en indices
    city_index = cities.index(inputs["city"])
    room_type_index = room_types.index(inputs["room_type"])
    season_index = seasons.index(inputs["season"])

    # Préparer les données pour le modèle
    input_data = pd.DataFrame({
        "city": [city_index],
        "room_type": [room_type_index],
        "seasons": [season_index],
        "minimum_nights": [inputs["minimum_nights"]],
        "num_people": [inputs["num_people"]]
    })

    # Prédire le prix
    return model.predict(input_data)[0]
