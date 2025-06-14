#streamlit_app.py

import streamlit as st

#configure la page principale
st.set_page_config(
    page_title="Bienvenue dans l'Appli E-commerce",
    layout="centered"
)

st.title("Bienvenue dans l'Application d'Analyse du Comportement Consommateur E-commerce")

st.markdown("""
Cette application interactive a été conçue pour explorer les tendances et les caractéristiques
d'un large jeu de données de transactions e-commerce.

Utilisez la barre latérale à gauche pour naviguer entre les différentes pages de notre application :
* **PAGE PRINCIPALE** : Aperçu des indicateurs clés (KPIs) et statistiques générales.
* **VISUALISATION INTERACTIVES** : Visualisations interactives avec filtres pour des analyses spécifiques.
* **ANALYSE GENERALES** : Graphiques et analyses globales du comportement du consommateur.

Nous espérons que cette application vous aidera à mieux comprendre les habitudes de commande et les préférences des clients.
""")

st.markdown("---")
st.info("Pour commencer, sélectionnez une page dans la barre de navigation à gauche.")

#bas de page
st.markdown("Application développée pour le projet Data Management par Monna, Liliane et Hugo")