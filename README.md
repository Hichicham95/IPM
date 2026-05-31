# 🤖 PADOC Mini-Projet IA — Prédiction T_pm MSAP

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange?logo=scikit-learn)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Formation Doctorale PADOC — Intelligence Artificielle**  
> ENP Alger — Année Universitaire 2025–2026

---

## 📋 Résumé

Prédiction de la **température des aimants permanents** ($T_{pm}$) d'un Moteur  
Synchrone à Aimants Permanents (MSAP) par Machine Learning, à partir des signaux  
électriques de fonctionnement (courants dq, tensions, vitesse, couple).

| Métrique | Gradient Boosting | Random Forest |
|----------|:-----------------:|:-------------:|
| **MAE**  | **0.289 °C**      | 0.212 °C      |
| **RMSE** | **1.405 °C**      | 1.459 °C      |
| **R²**   | **0.9910**        | 0.9903        |

---

## 🗂️ Structure du projet

```
PADOC_IA_Project/
├── data/
│   └── dataset.csv              # Dataset (50k échantillons synthétiques)
├── figures/
│   ├── fig1_distributions.png   # Histogrammes
│   ├── fig2_boxplots.png        # Boxplots
│   ├── fig3_correlation.png     # Heatmap corrélation
│   ├── fig4_scatter.png         # Scatter plots
│   ├── fig5_time_series.png     # Séries temporelles
│   ├── fig6_predictions.png     # Résultats modèle
│   ├── fig7_feature_importance.png
│   └── fig8_model_comparison.png
├── results/
│   ├── metrics.csv              # Tableau comparatif des métriques
│   └── best_model.pkl           # Modèle sauvegardé (Gradient Boosting)
├── src/
│   ├── 01_data_generation.py    # Étape 1 : Données
│   ├── 02_eda.py                # Étapes 2-4 : EDA
│   └── 03_train_evaluate.py     # Étapes 5-9 : ML Pipeline
├── report/
│   └── rapport_PADOC_IA.tex     # Rapport LaTeX complet
├── run_all.py                   # 🚀 Script principal (lance tout)
├── requirements.txt
└── README.md
```

---

## 🚀 Lancement rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/[username]/PADOC-IA-MSAP
cd PADOC-IA-MSAP

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le pipeline complet
python run_all.py
```

---

## 📊 Pipeline ML (10 étapes)

```
Données → EDA → Prétraitement → Split → Modèle → Entraînement → Évaluation → Analyse
```

1. **Génération/Chargement** — données synthétiques physiques ou Kaggle réel
2. **Statistiques descriptives** — moyenne, médiane, variance, corrélation  
3. **Visualisations EDA** — histogrammes, boxplots, heatmaps, scatter plots
4. **Prétraitement** — gestion outliers, ingénierie de features physiques
5. **Séparation 70/15/15** — Train / Validation / Test
6. **Construction modèles** — LR, Random Forest, Gradient Boosting
7. **Entraînement** — Pipeline scikit-learn avec StandardScaler
8. **Évaluation** — MAE, RMSE, R²
9. **Visualisations résultats** — réel vs prédit, erreurs, importance features
10. **Analyse et discussion** — limites, améliorations futures

---

## 🔗 Dataset réel (optionnel)

```
https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature
```
Placer `pmsm_temperature_data.csv` dans `data/` et mettre `USE_REAL_DATA = True`
dans `src/01_data_generation.py`.

---

## 👤 Auteur

**[Votre Nom]** — Doctorant, Laboratoire de Génie Électrique, ENP Alger  
Encadrant : Pr. Boughrara Kamel | Co-encadrant : Dr. Ladghem-Chikouche Brahim
