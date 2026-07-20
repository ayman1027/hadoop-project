import streamlit as st

st.title("Prédiction du GPA — Impact de l'IA sur les étudiants")

st.write("Renseigne les infos de l'étudiant pour prédire son GPA de fin de semestre.")

# Coefficients trouvés par notre régression linéaire (calculée dans le notebook)
a1 = 0.0001881948890953249   # poids Weekly_GenAI_Hours
a2 = 0.013279717267157385    # poids Traditional_Study_Hours
b = 3.1988574104584497        # constante

# Formulaire de saisie
heures_ia = st.slider("Heures d'usage de l'IA par semaine", 0.0, 40.0, 8.0)
heures_travail = st.slider("Heures de travail classique par semaine", 0.0, 40.0, 11.0)

# Calcul de la prédiction avec notre formule
gpa_predit = a1 * heures_ia + a2 * heures_travail + b

st.subheader(f"GPA prédit : {gpa_predit:.2f}")

st.caption("Modèle : régression linéaire codée à la main (équation normale), RMSE ≈ 0.49")