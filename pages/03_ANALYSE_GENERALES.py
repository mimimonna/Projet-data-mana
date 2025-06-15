#pages/03_ANALYSE_GENERALES.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#IMPORTANT 
from utils import load_data

#la page Streamlit
st.set_page_config(layout="wide", page_title="Analyse E-commerce - Analyses Générales")

df = load_data()

#recalculs pour les KPIs nécessaires à la page qui ne sont pas filtrés
pourcentage_vip = df['Client_VIP'].mean() * 100
pourcentage_bestsellers = df['Produit bestseller'].mean() * 100

st.title("Analyses Générales du Comportement Consommateur")
st.markdown("Cette page présente des analyses basées sur l'ensemble du jeu de données sans l'application de filtres interactifs.")

st.markdown("---")

#graphiques du notebook
#colonne pour les 2 pie charts
col_pie1, col_pie2 = st.columns(2)

with col_pie1:
    #graphique 8 :Les clients VIP
    st.subheader("Les Clients VIP")
    st.write("Ce graphique montre la proportion de clients ayant passé plus de 50 commandes sur l'ensemble du jeu de données sans filtre ajoutés.")
    labels_pie_vip = ['Clients non VIP', 'Clients VIP']
    sizes_pie_vip = [100 - pourcentage_vip, pourcentage_vip]
    colors_pie_vip = ['#77DD77', '#AEC6CF']

    fig2, ax2 = plt.subplots()
    ax2.pie(
        sizes_pie_vip,
        labels=labels_pie_vip,
        colors=colors_pie_vip,
        autopct='%1.1f%%',
        startangle=90
    )
    ax2.axis('equal')
    plt.title('Répartition des Clients VIP vs Clients Non VIP')
    st.pyplot(fig2)

with col_pie2:
    #graphique 9 : Les produits bestsellers
    st.subheader("Les Produits Bestsellers")
    st.write("Ce graphique montre la proportion de produits ayant été commandés plus de 200 000 fois sur l'ensemble du jeu de données sans filtre ajoutés.")
    labels_pie_bestseller = ['Non-Bestsellers', 'Bestsellers']
    sizes_pie_bestseller = [100 - pourcentage_bestsellers, pourcentage_bestsellers]
    colors_pie_bestseller = ['lightblue', 'hotpink']

    fig4, ax4 = plt.subplots()
    ax4.pie(
        sizes_pie_bestseller,
        labels=labels_pie_bestseller,
        colors=colors_pie_bestseller,
        startangle=90,
        autopct='%1.1f%%',
        wedgeprops={'width': 0.5}
    )
    ax4.axis('equal')
    plt.title('Répartition des Produits Bestsellers')
    st.pyplot(fig4)

st.markdown("---")

#graphique 7 : Distribution des commandes par heure de la journée
st.subheader("Nombre de commandes par heure de la journée")
st.write("Vue d'overview du nombre total des commandes par heure de la journée sur l'ensemble du dataset.")
commandes_total_par_heure = df['order_hour_of_day'].value_counts().sort_index().reset_index(name='Nombre de commandes')
commandes_total_par_heure.columns = ['Heure de la journée', 'Nombre de commandes']

fig7 = px.line(
    commandes_total_par_heure,
    x='Heure de la journée',
    y='Nombre de commandes',
    title='Nombre total de commandes par heure de la journée'
)
fig7.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=1))
col1, col2, col3 = st.columns([1, 3, 1])
with col2: # Place le contenu suivant (le graphique) à l'intérieur de la colonne du milieu.
    st.plotly_chart(fig7, use_container_width=True)

#bas de page
st.markdown("---")
st.markdown("---")
st.markdown("Application développée pour le projet Data Management par Monna, Liliane et Hugo")