import streamlit as st
from sidebar import render_sidebar
from utils import predict_price
from chatbot import render_chat
from config.cities import cities
from config.city_images import city_images
from config.options import room_types, seasons


def main():
    st.set_page_config(page_title="Prédiction des prix Airbnb", layout="wide", initial_sidebar_state="expanded")

    # Afficher la barre latérale
    user_inputs = render_sidebar(cities, room_types, seasons)

    # Titre et description
    st.title("Prédiction des prix Airbnb")
    st.write("Prédisez le prix de votre logement et posez vos questions à notre assistant intelligent.")

    # images associées à la ville sélectionnée
    selected_city = user_inputs["city"]
    images = city_images.get(selected_city, ["assets/house1.jpg", "assets/house2.jpg"])

    # Affichage des images
    col1, col2 = st.columns(2)
    col1.image(images[0], use_container_width=True)
    col2.image(images[1], use_container_width=True)
    
    # Images côte à côte
    #col1, col2 = st.columns(2)
    #col1.image("assets/house1.jpg", use_container_width=True)
    #col2.image("assets/house2.jpg", use_container_width=True)

    # Section de prédiction des prix
    st.header("Prédiction des prix")
    if user_inputs["submit"]:
        predicted_price = predict_price(user_inputs)
        st.markdown(
            f"""
            <div style="text-align: center; font-weight: bold; font-size: 18px;">
                <p><h5>Données saisies :</h5></p>
                <ul>
                    <li>Ville : {user_inputs["city"]}</li>
                    <li>Type de logement : {user_inputs["room_type"]}</li>
                    <li>Saison : {user_inputs["season"]}</li>
                    <li>Nombre de nuits minimum : {user_inputs["minimum_nights"]}</li>
                    <li>Nombre de personnes : {user_inputs["num_people"]}</li>
                </ul>
                <p style="color: green;">Le prix prédit pour votre logement est : {predicted_price:.2f} €</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Veuillez ajuster les paramètres dans la barre latérale et cliquer sur Prédire le prix.")

    # Lien vers Power BI
    st.markdown(
        """
        ### Tableau de bord Power BI
        Consultez notre tableau de bord interactif pour plus d'analyses sur les prix des logements Airbnb :
        [Consultez le Dashboard](https://app.powerbi.com/groups/me/reports/62cb6eb5-1725-4434-bbc1-cef66de8964a/de2f6777deea833daaa4?redirectedFromSignup=1&experience=power-bi)
        """,
        unsafe_allow_html=True
    )

    # Section du chatbot
    render_chat()

if __name__ == "__main__":
    main()
