#utils.py

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    """Charge le dataset à partir du fichier CSV."""
    try:
        file_path = 'new_ECommerce_consumer_behaviour.csv'
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Erreur : Le fichier '{file_path}' est introuvable. il faut recommencer.")
        st.stop()