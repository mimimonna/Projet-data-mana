#pages/02_VISUALISATION_INTERACTIVES.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#IMPORTANT!!
from utils import load_data

#la page Streamlit
st.set_page_config(layout="wide", page_title="Analyse E-commerce - Visualisations")

df = load_data()

#barre latérale pour les filtres
st.sidebar.header("Filtres d'analyse")

#jjour de la semaine
jours_mapping = {0: 'Dimanche', 1: 'Lundi', 2: 'Mardi', 3: 'Mercredi', 4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi'}
selected_day_number = st.sidebar.selectbox(
    "Sélectionnez un jour de la semaine",
    sorted(df['order_dow'].unique()),
    format_func=lambda x: jours_mapping.get(x, f"Jour inconnu ({x})")
)
#afficher les clients VIP
filter_vip = st.sidebar.checkbox("Clients VIP", value=False)

#filtrer par rayon des produits
departments = sorted(df['department'].unique())
selected_department = st.sidebar.selectbox("Filtrer par rayons", ['Tous'] + departments)
filtered_df = df.copy() 

#filtre Jour de la Semaine qui est utilisé pour le graphique des horaire
filtered_df_day = filtered_df[filtered_df['order_dow'] == selected_day_number].copy()

#le filtre VIP
if filter_vip:
    filtered_df = filtered_df[filtered_df['Client_VIP'] == 1].copy()

#ke filtre rayon
if selected_department != 'Tous':
    filtered_df = filtered_df[filtered_df['department'] == selected_department].copy()

#filtered_df est maintenant le DataFrame utilisé pour la plupart des graphiques,
#filtre par VIP et rayons. filtered_df_day est pour le graphique horaire

#visualisations interactives
st.header("Visualisations interactives")
st.markdown("Explorez les tendances du comportement consommateur à l'aide des graphiques ci-dessous. Utilisez les filtres dans la barre latérale pour affiner l'analyse.")

#disposition en colonnes pour certains graphiques
#crée 2 colonnes pour placer 2 graphiques côte à côte
viz_col1, viz_col2 = st.columns(2)

with viz_col1:
    #graphique 1 : Distribution des commandes par heure pour le jour
    if selected_day_number in jours_mapping:
        if selected_day_number in jours_mapping:
            st.subheader(f"Commandes par heure ({jours_mapping[selected_day_number]})")
        else:
            st.error("Erreur : Le jour sélectionné n'est pas valide.")
        st.write(f"Répartition horaire des commandes pour le {jours_mapping[selected_day_number]}{' (Clients VIP)' if filter_vip else ''}{f' dans le rayon {selected_department}' if selected_department != 'Tous' else ''}.")
    else:
        st.error("Erreur : Le jour sélectionné n'est pas valide.")

    #re-appliquer les filtres pour VIP et rayon au DF horaire
    filtered_df_hour_viz = filtered_df_day.copy()
    if filter_vip:
         filtered_df_hour_viz = filtered_df_hour_viz[filtered_df_hour_viz['Client_VIP'] == 1].copy()
    if selected_department != 'Tous':
        filtered_df_hour_viz = filtered_df_hour_viz[filtered_df_hour_viz['department'] == selected_department].copy()

    commandes_par_heure = filtered_df_hour_viz['order_hour_of_day'].value_counts().sort_index().reset_index(name='Nombre de commandes')
    commandes_par_heure.columns = ['Heure de la journée', 'Nombre de commandes']

    if not commandes_par_heure.empty:
        fig1 = px.bar(
            commandes_par_heure,
            x='Heure de la journée',
            y='Nombre de commandes',
            title=f"Commandes par heure ({jours_mapping[selected_day_number]})",
            labels={'Heure de la journée': 'Heure', 'Nombre de commandes': 'Nb de commandes'}
        )
        fig1.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=1))
        st.plotly_chart(fig1, use_container_width=True) #use_container_width=True ajuste le graphique
    else:
        st.info("Aucune donnée de commande pour les filtres sélectionnés pour cette analyse horaire.")

with viz_col2:
    #graphique 6 : distribution des commandes par jour de la semaine
    st.subheader(f"Commandes par jour de la semaine{'' if filter_vip or selected_department != 'Tous' else ''}")
    st.write("Nombre de commandes par jour de la semaine selon les filtres")

    #utilisez le DF filtrer par VIP et rayon pour ce graphique
    commandes_par_jour = filtered_df['order_dow'].map(jours_mapping).value_counts().reindex(jours_mapping.values()).reset_index(name='Nombre de commandes')
    commandes_par_jour.columns = ['Jour de la semaine', 'Nombre de commandes']

    if not commandes_par_jour.empty:
        fig6 = px.bar(
            commandes_par_jour,
            x='Jour de la semaine',
            y='Nombre de commandes',
            title='Nombre de commandes par jour de la semaine',
            labels={'Jour de la semaine': 'Jour', 'Nombre de commandes': 'Nb de commandes'}
        )
        st.plotly_chart(fig6, use_container_width=True)
    else:
        st.info("Aucune donnée de commande pour les filtres sélectionnés.")

st.markdown("---")

#les autres disposition des colonnes
viz_col3, viz_col4 = st.columns(2)

with viz_col3:
    #graphique 3 : Top 10 produits les plus commandés
    st.subheader(f"Top 10 Produits Commandés{'' if filter_vip or selected_department != 'Tous' else ''}")
    st.write("Les produits les plus fréquents dans les commandes selon les filtres appliqués.")
    top_products = (
        filtered_df.groupby('product_name')['user_id']
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name='Nombre de commandes')
    )
    if not top_products.empty:
        fig3 = px.bar(
            top_products,
            x='product_name',
            y='Nombre de commandes',
            title=f"Top 10 des Produits Commandés{'' if filter_vip or selected_department != 'Tous' else ''}",
            color='product_name',
            labels={'product_name': 'Nom du produit', 'Nombre de commandes': 'Nombre de commandes'},
        )
        fig3.update_layout(
            xaxis_tickangle=-45,
            xaxis_title='Nom du produit',
            yaxis_title='Nombre de commandes',
            showlegend=False,
            height=500,
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Aucune donnée de produit trouvée pour les filtres sélectionnés.")

with viz_col4:
    #graphique 5 : Fréquence de Commande moyenne par Client
    st.subheader(f"Fréquence Moyenne de Commande{'' if filter_vip or selected_department != 'Tous' else ''}")
    st.write("Distribution du délai moyen en jours entre deux commandes pour les clients filtrés.")

    #on calcule le délai moyen pour les clients filtrés
    #on filtre sur user_id dans filtered_df puis on calcule la moyenne sur le DF
    #pour avoir le délai moyen global pour des clients.
    #si on veut le délai moyen mais uniquement sur les commandes filtrées on utilise filtered_df
    delai_moyen_par_client = filtered_df.groupby('user_id')['days_since_prior_order'].mean().dropna() #dropna() pour les clients avec une seule commande

    if not delai_moyen_par_client.empty:
        fig5, ax5 = plt.subplots(figsize=(10, 6))
        sns.histplot(
            delai_moyen_par_client,
            bins=50,
            kde=True,
            color='#FF4C4C',
            ax=ax5
        )

        ax5.set_title(f"Fréquence Moyenne de Commande par Client{'' if filter_vip or selected_department != 'Tous' else ''}", fontsize=15)
        ax5.set_xlabel('Délai moyen entre deux commandes (en jours)', fontsize=12)
        ax5.set_ylabel('Nombre de clients', fontsize=12)
        ax5.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(fig5)
    else:
        st.info("Aucune donnée de délai moyen pour les clients selon les filtres.")


#bas de page
st.markdown("---")
st.markdown("---")
st.markdown("Application développée pour le projet Data Management par Monna, Liliane et Hugo")