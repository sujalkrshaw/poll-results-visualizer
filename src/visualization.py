import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def plot_all(df):
    os.makedirs("outputs", exist_ok=True)

    # Bar
    sns.countplot(x="Preferred_Tool", data=df)
    plt.title("Preferred Tool Distribution")
    plt.savefig("outputs/bar.png")
    plt.clf()

    # Pie
    df['Preferred_Tool'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Tool Usage Share")
    plt.ylabel("")
    plt.savefig("outputs/pie.png")
    plt.clf()

    # Region
    pd.crosstab(df['Region'], df['Preferred_Tool']).plot(kind='bar', stacked=True)
    plt.title("Region vs Preferred Tool")
    plt.savefig("outputs/region.png")
    plt.clf()