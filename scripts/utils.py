
def data_import(file_path):
    import pandas as pd  # Import de la bibliothèque pandas

    try:
        # Lecture du fichier Excel
        df = pd.read_excel(file_path, sheet_name="distance")
        print(df.head())  # Affiche les 5 premières lignes du DataFrame
        return df  # Retourne le DataFrame pour une utilisation ultérieure
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None


def removed(df):
    # Si vous voulez supprimer les lignes contenant au moins une valeur manquante
    cleaned_df = df.dropna(how="any")
    
    # Affiche le nombre de lignes supprimées
    removed_rows = len(df) - len(cleaned_df)
    print(f"{removed_rows} ligne(s) vide(s) supprimée(s).")
    print("\n\n")
    return cleaned_df

def bonjour():
    return "Hello world !"