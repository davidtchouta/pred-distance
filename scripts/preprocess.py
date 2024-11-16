import pandas as pd
from utils import data_import, removed

# Appel de la fonction avec un chemin de fichier
file_path = "../data/perf_kilo.xlsx"




if __name__ == "__main__":
    # Étape 1 : Importer les données
    data = data_import(file_path)
    if data is not None:
        print("Importation réussie !")
    else:
        print("Échec de l'importation.")
    # Étape 2 : Nettoyer les données en supprimant les lignes vides
    cleaned_df = removed(data)
    cleaned_df.to_csv('../data/processed_data.csv', index=False)
    cleaned_df.info()

