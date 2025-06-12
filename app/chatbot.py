import openai
import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_chat import message

load_dotenv()

# Initialisation de l'API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("La clé API OpenAI est manquante ou incorrecte.")

def get_bot_response(user_input):
    """Appelle l'API OpenAI pour générer une réponse."""
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"""Tu es un assistant intelligent, réponds uniquement aux questions liées aux logement AirBNB en France. 
                      Réponds de manière naturelle : {user_input}""",
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erreur : {str(e)}"

def render_chat():
    """Affiche l'interface de chat."""
    st.title("Chatbot AirBNB")
    st.write("Posez vos questions à notre assistant IA.")
    
    # Initialiser l'historique
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Formulaire pour l'entrée utilisateur
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Votre question :", key="user_input")
        submit_button = st.form_submit_button("Envoyer")

    if submit_button and user_input.strip():
        # Ajouter l'entrée utilisateur et la réponse du bot
        st.session_state.messages.append({"role": "user", "content": user_input})
        bot_response = get_bot_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": bot_response})

    # Affichage des messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            message(msg["content"], is_user=True)
        else:
            message(msg["content"])

