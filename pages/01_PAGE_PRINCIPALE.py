#pages/01_PAGE_PRINCIPALE.py

#on importe les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#IMPORTANT
from utils import load_data

#la page Streamlit
st.set_page_config(layout="wide", page_title="Analyse E-commerce - Page Principale")

#chargement des données
df = load_data()

#vérifier les colonnes nécessaires
required_cols = ['Client_VIP', 'Produit bestseller', 'order_dow', 'order_hour_of_day', 'product_name', 'days_since_prior_order', 'user_id', 'department', 'reordered']
if not all(col in df.columns for col in required_cols):
    missing = [col for col in required_cols if col not in df.columns]
    st.error(f"Erreur : Les colonnes sont manquantes dans le fichier CSV chargé. Colonnes manquantes : {missing}")
    st.write("il faut sassurer que le notebook a été exécuté complètement et que le fichier csv a été exporté.")
    st.stop()

#recalculs pour les KPIs (indicateurs clés)
total_orders = df.shape[0]
unique_users = df['user_id'].nunique()
average_reorder_rate = df['reordered'].mean() * 100
pourcentage_vip = df['Client_VIP'].mean() * 100
pourcentage_bestsellers = df['Produit bestseller'].mean() * 100

#titre principal de l'appli
st.title("Analyse du comportement des consommateurs dans le e-commerce")
st.markdown("Cette application explore les tendances et les caractéristiques d'un large jeu de données de transactions e-commerce.")

#indicateurs Clés (KPIs)
st.header("Indicateurs Clés")

#les colonnes pour afficher les KPIs côte à côte
col1, col2, col3, col4, col5 = st.columns(5) #on rée 5 colonnes égale

with col1:
    st.metric(label="Total des Commandes", value=f"{total_orders:,}".replace(",", " "))
with col2:
    st.metric(label="Clients Uniques", value=f"{unique_users:,}".replace(",", " "))
with col3:
    st.metric(label="Taux de Re-commande Moyen", value=f"{average_reorder_rate:.2f} %")
with col4:
    st.metric(label="% Clients VIP", value=f"{pourcentage_vip:.2f} %")
with col5:
    st.metric(label="% Produits Bestsellers", value=f"{pourcentage_bestsellers:.2f} %")

st.markdown("---")

#statistiques
st.header("Statistiques")
st.write("Voici un résumé statistique des variables numériques clés du jeu de données:")
st.write("Statistiques sur l'ensemble du jeu de données :")
st.write(df.describe())

#bas de page
st.markdown("---")
st.markdown("---")
st.markdown("Application développée pour le projet Data Management par Monna, Liliane et Hugo")