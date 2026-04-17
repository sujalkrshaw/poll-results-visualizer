import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["Preferred_Tool"] = df["Preferred_Tool"].str.strip().str.title()
    df["Satisfaction"] = pd.to_numeric(df["Satisfaction"], errors='coerce')

    df.to_csv("data/cleaned_poll_data.csv", index=False)
    return df