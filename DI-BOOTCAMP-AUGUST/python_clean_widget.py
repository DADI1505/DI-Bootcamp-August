import os
import json

def clean_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Supprime les métadonnées widgets qui posent problème
    if 'metadata' in nb and 'widgets' in nb['metadata']:
        del nb['metadata']['widgets']
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

# Parcourt tous les dossiers pour trouver les .ipynb
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            print(f"Nettoyage de : {os.path.join(root, file)}")
            clean_notebook(os.path.join(root, file))