# Video Game Sales Predictor

Ett AI/ML-projekt som förutsäger global försäljning för tv-/datorspel baserat på plattform, genre och utgivningsår.

Projektet genomfört som del av kunskapskontrollen i kursen *AI - teori och tillämpning, del 1*.

## Om projektet

Vi använder datasetet [Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales) från Kaggle (~16 500 spel, 1980–2020) och bygger ett komplett fullstack AI/ML-flöde:

1. **Datastädning** – rensning av saknade värden i rådatan (pandas)
2. **Databas** – rensad data lagras i en SQLite-databas (backend)
3. **Modellering** – en Random Forest-modell tränas för att förutsäga global försäljning
4. **Frontend** – ett Streamlit-gränssnitt där man kan välja plattform, genre och år och få en förutsägelse

## Teknisk stack

- Python, pandas, scikit-learn
- SQLite
- Streamlit
- Git/GitHub (branches + pull requests)

## Så kör du projektet lokalt

Klona repot:

    git clone git@github.com:mannilowman/VideoGameSales-ML.git
    cd VideoGameSales-ML

Skapa och aktivera virtuell miljö:

    python -m venv venv
    source venv/Scripts/activate   # Windows (Git Bash)

Installera beroenden:

    pip install -r requirements.txt

Starta Streamlit-appen:

    streamlit run app/streamlit_app.py

Appen öppnas på `http://localhost:8501`.

## Mappstruktur

    data/raw/          Orörd originaldata
    data/processed/    Rensad data
    database/          Script för att skapa SQLite-databasen
    notebooks/         Utforskning, datastädning och modellträning
    models/            Sparad tränad modell och encoders
    app/               Streamlit-frontend
    report/            Teknisk rapport (PDF)

## Resultat

Modellen uppnår ett MAE på cirka 0,59 miljoner sålda exemplar och ett R² nära 0,00. Se rapporten för en fullständig analys och diskussion av modellens begränsningar.

## Utvecklat av
Emmanuel & Mohammed