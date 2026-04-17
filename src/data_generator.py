import pandas as pd
import numpy as np

def generate_data(n=300):
    np.random.seed(42)

    data = {
        "User_ID": range(1, n + 1),

        "Age_Group": np.random.choice(
            ["18-24", "25-34", "35-44"], n
        ),

        "Gender": np.random.choice(
            ["Male", "Female"], n
        ),

        "Region": np.random.choice(
            ["East", "West", "North", "South"], n
        ),

        # Bias added (realistic simulation)
        "Preferred_Tool": np.random.choice(
            ["Python", "Excel", "R", "Power BI"],
            n,
            p=[0.4, 0.3, 0.1, 0.2]
        ),

        "Satisfaction": np.random.randint(1, 6, n),

        "Feedback": np.random.choice(
            [
                "Great tool",
                "Very useful",
                "Excellent",
                "Needs improvement",
                "Not bad",
                "Could be better"
            ],
            n
        ),

        # ✅ NEW: TIMESTAMP COLUMN (IMPORTANT)
        "Timestamp": pd.date_range(
            start="2024-01-01",
            periods=n,
            freq="h"
        )
    }

    df = pd.DataFrame(data)

    # Save raw dataset
    df.to_csv("data/raw_poll_data.csv", index=False)

    return df