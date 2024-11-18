import pandas as pd
from utils import data_import, removed, determine_season

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
    #cleaned_df.info()
    #ajouter la colonne season
    # Appliquer la fonction determine_season à la colonne 'day'
    cleaned_df['season'] = cleaned_df['day'].apply(determine_season)
    # Afficher le DataFrame avec les saisons
    print(cleaned_df)
    


