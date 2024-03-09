import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Fonctions de calcul des indicateurs
def calcul_tdr(nombre_risques_identifies, nombre_risques_total):
    return nombre_risques_identifies / nombre_risques_total

def calcul_ttr(nombre_risques_traites, nombre_risques_identifies):
    return nombre_risques_traites / nombre_risques_identifies

def calcul_tnrr(niveau_moyen_apres_traitement, niveau_moyen_initiaux):
    return niveau_moyen_apres_traitement / niveau_moyen_initiaux

def calcul_temps_moyen_resolution(sum_temps_resolution, nombre_risques_traites):
    return sum_temps_resolution / nombre_risques_traites

# Interface utilisateur Streamlit
st.title("Tableau de bord des Indicateurs de Performance - RISK@SMSI-CRNS")

# Saisie des données
nombre_risques_identifies = st.number_input("Nombre de risques identifiés", min_value=0, step=1)
nombre_risques_total = st.number_input("Nombre total de risques", min_value=1, step=1)
nombre_risques_traites = st.number_input("Nombre de risques traités", min_value=0, step=1)
niveau_moyen_apres_traitement = st.number_input("Niveau moyen des risques après traitement", min_value=0.0, step=0.1)
niveau_moyen_initiaux = st.number_input("Niveau moyen des risques initiaux", min_value=0.0, step=0.1)
sum_temps_resolution = st.number_input("Somme des temps de résolutions des risques", min_value=0, step=1)

# Bouton pour générer le tableau de bord
if st.button("KPI Dashboard"):
    # Calcul des indicateurs
    tdr = calcul_tdr(nombre_risques_identifies, nombre_risques_total)
    ttr = calcul_ttr(nombre_risques_traites, nombre_risques_identifies)
    tnrr = calcul_tnrr(niveau_moyen_apres_traitement, niveau_moyen_initiaux)
    temps_moyen_resolution = calcul_temps_moyen_resolution(sum_temps_resolution, nombre_risques_traites)

    # Création d'un DataFrame pour le pie chart
    data = {
        'Indicateur': ['Taux de Détection des Risques (TDR)', 'Taux de Traitement des Risques (TTR)', 'Taux de réduction de Risque Résiduel (TNRR)', 'Temps Moyen de Réduction des Risques (TMR)'],
        'Valeur': [tdr, ttr, tnrr, temps_moyen_resolution]
    }
    df = pd.DataFrame(data)

    # Affichage du DataFrame
    st.table(df)

    # Création du pie chart
    fig, ax = plt.subplots()
    ax.pie(df['Valeur'], labels=df['Indicateur'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Affichage du pie chart
    st.pyplot(fig)
