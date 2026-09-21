import sqlite3
import pandas as pd

# Läs in den rensade datan
df = pd.read_csv('../data/processed/vgsales_clean.csv')

# Skapa (eller anslut till) databasen
conn = sqlite3.connect('vgsales.db')

# Skriv DataFramen till en tabell i databasen
df.to_sql('games', conn, if_exists='replace', index=False)

conn.close()

print("Klart! Databasen är skapad.")