import pandas as pd

print("Projet NASA - Feux de forêt France")

try:
    df = pd.read_csv("data/fires_france.csv")

    print("\nAperçu des données :")
    print(df.head())

    print("\nNombre de lignes :", len(df))
    print("\nColonnes :")
    print(df.columns.tolist())

except FileNotFoundError:
    print("Le fichier data/fires_france.csv est introuvable.")