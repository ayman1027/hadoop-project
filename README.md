3. Nettoyage (vérification doublons/valeurs manquantes)
4. Statistiques descriptives
5. Machine Learning : régression linéaire codée à la main (équation normale, sans librairie ML), pour prédire le GPA à partir des heures d'usage IA et de travail classique
6. Data Viz : graphiques matplotlib
7. Dashboard Streamlit pour tester le modèle avec des valeurs personnalisées

## Installation

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Copier `.env.example` en `.env` et renseigner le chemin de son JDK et l'URI HDFS.

## Lancer

Notebook : `jupyter notebook main.ipynb`

Dashboard : `streamlit run app.py`
YARN
http://localhost:8088 → interface du ResourceManager
