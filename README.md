# Projet-data-mana

# Analyse du Comportement des Consommateurs E-commerce

## À Propos du Projet

Ce projet **Streamlit interactif** a été développé pour analyser le comportement des consommateurs sur une plateforme d'e-commerce.  
Il permet d'explorer des tendances clés, d'identifier des produits best-sellers, de comprendre les habitudes de commande et de visualiser des données importantes comme la répartition des clients VIP.  
L’objectif est d'offrir une interface utilisateur simple pour naviguer à travers différentes analyses et obtenir des informations clés sur les données e-commerce.

---

## Fonctionnalités

- **Page principale** : Aperçu des indicateurs clés de performance (KPIs) et statistiques générales du jeu de données.
- **Visualisations interactives** : Graphiques dynamiques avec des filtres (jour de la semaine, clients VIP, rayons de produits) pour affiner l'analyse.
- **Analyses générales** : Visualisations globales du comportement des consommateurs, incluant la répartition des clients VIP et des produits best-sellers.

---

## Technologies Utilisées

- **Python**
- **Streamlit** : pour créer l'interface utilisateur web interactive.
- **Pandas** : pour la manipulation et l'analyse des données.
- **NumPy** : pour les opérations numériques.
- **Matplotlib / Seaborn** : pour la création de visualisations statiques.
- **Plotly Express** : pour la création de visualisations interactives.

---

## Comment Lancer l'Application

Suivez ces étapes avant de lancer l'application :

1. Télécharger le dossier ZIP du projet.
2. Ne **pas changer le nom** du dossier principal `Projet_data_mana/`, sinon cela modifiera les chemins vers les pages.

### Structure du Projet

```
Projet_data_mana/
├── Appli_streamlit/
│   ├── .streamlit/                     #Pour lancer l’application : streamlit run streamlit_app.py
│   │   └── config.toml                 #Configuration de l'apparence Streamlit
│   ├── pages/                          #Contient les différentes pages de l'application
│   │   ├── 01_PAGE_PRINCIPALE.py
│   │   ├── 02_VISUALISATION_INTERACTIVES.py
│   │   └── 03_ANALYSE_GENERALES.py
│   ├── new_ECommerce_consumer_behaviour.csv  #Jeu de données utilisé
│   ├── streamlit_app.py                #Point d'entrée principal de l'application
│   └── utils.py                        #Fonctions utilitaires
├── Projet_DataMgt.ipynb                #Notebook Jupyter
├── ECommerce_consumer_behaviour.csv    #Copie du jeu de données
└── requirements.txt                    #Fichier des dépendances
```
                
### Installer les dépendances

```bash
pip install -r requirements.txt


