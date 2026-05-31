"""
==============================================================================
  PADOC Mini-Projet IA – SCRIPT PRINCIPAL (run_all.py)
  Lance le pipeline complet en une seule commande :
    python run_all.py

  Prérequis :
    pip install numpy pandas matplotlib seaborn scikit-learn joblib
==============================================================================
"""

import subprocess, sys, os
from pathlib import Path

# ── Installer les dépendances si nécessaires ───────────────────────────────
def install_deps():
    deps = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'joblib']
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet'] + deps)

# ── Lancer les scripts dans l'ordre ────────────────────────────────────────
def run_step(script: str, label: str):
    print(f"\n{'='*60}")
    print(f"  ► {label}")
    print(f"{'='*60}")
    src_dir = Path(__file__).parent / 'src'
    result  = subprocess.run([sys.executable, src_dir / script], capture_output=False)
    if result.returncode != 0:
        print(f"[ERREUR] {script} a échoué (code {result.returncode})")
        sys.exit(1)

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)

    print("\n" + "█"*60)
    print("  PADOC MINI-PROJET IA – Pipeline Complet")
    print("  Prédiction T_pm  MSAP – ENP Alger 2025-2026")
    print("█"*60)

    print("\n[0] Installation des dépendances...")
    install_deps()

    run_step("01_data_generation.py",  "Étape 1 : Génération / Chargement des données")
    run_step("02_eda.py",              "Étapes 2-4 : EDA & Visualisations")
    run_step("03_train_evaluate.py",   "Étapes 5-10 : Prétraitement, Modélisation, Évaluation")

    print("\n" + "█"*60)
    print("  ✅  PIPELINE TERMINÉ !")
    print("  📁  Figures  → figures/")
    print("  📊  Métriques → results/metrics.csv")
    print("  🤖  Modèle   → results/best_model.pkl")
    print("█"*60 + "\n")
