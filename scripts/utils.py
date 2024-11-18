
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

# function for debugging purpose
def bonjour():
    return "Hello world !"

# adding a saison period variable



def determine_season(day):
    from datetime import datetime
    # Définir les intervalles saisonniers
    summer_intervals = [
        (datetime(2021, 6, 18), datetime(2021, 9, 20)),
        (datetime(2022, 6, 21), datetime(2022, 9, 20)),
        (datetime(2023, 6, 21), datetime(2023, 9, 20)),
        (datetime(2024, 6, 21), datetime(2024, 9, 20)),
    ]

    autumn_intervals = [
        (datetime(2021, 9, 21), datetime(2021, 12, 20)),
        (datetime(2022, 9, 21), datetime(2022, 12, 20)),
        (datetime(2023, 9, 21), datetime(2023, 12, 20)),
        (datetime(2024, 9, 21), datetime(2024, 11, 14)),  # Fin limitée à 14/11/2024
    ]

    winter_intervals = [
        (datetime(2021, 12, 21), datetime(2022, 3, 20)),
        (datetime(2022, 12, 21), datetime(2023, 3, 20)),
        (datetime(2023, 12, 21), datetime(2024, 3, 20)),
    ]

    spring_intervals = [
        (datetime(2022, 3, 21), datetime(2022, 6, 20)),
        (datetime(2023, 3, 21), datetime(2023, 6, 20)),
        (datetime(2024, 3, 21), datetime(2024, 6, 20)),
    ]

    # Vérifier dans quelle saison la date se trouve
    for start, end in summer_intervals:
        if start <= day <= end:
            return "Été"
    for start, end in autumn_intervals:
        if start <= day <= end:
            return "Automne"
    for start, end in winter_intervals:
        if start <= day <= end:
            return "Hiver"
    for start, end in spring_intervals:
        if start <= day <= end:
            return "Printemps"

    return "Date hors période spécifiée"
