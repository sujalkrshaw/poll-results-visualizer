import pandas as pd

def analyze_data(df):
    results = {}

    results["tool_counts"] = df["Preferred_Tool"].value_counts()
    results["tool_percentage"] = (results["tool_counts"] / len(df)) * 100

    results["region_analysis"] = pd.crosstab(df["Region"], df["Preferred_Tool"])

    results["avg_satisfaction"] = df["Satisfaction"].mean()

    return results