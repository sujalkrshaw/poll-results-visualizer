from src.data_generator import generate_data
from src.preprocessing import clean_data
from src.analysis import analyze_data
from src.visualization import plot_all
from src.sentiment import apply_sentiment

# Step 1: Generate Data
df = generate_data()

# Step 2: Clean Data
df = clean_data(df)

# Step 3: Sentiment
df = apply_sentiment(df)

df.to_csv("data/cleaned_poll_data.csv", index=False)

# Step 4: Analysis
results = analyze_data(df)

# Step 5: Visualization
plot_all(df)

# Step 6: Insights
print("Most Preferred Tool:", results["tool_counts"].idxmax())
print("Average Satisfaction:", results["avg_satisfaction"])