import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(page_title="Poll Visualizer", layout="wide")

# ------------------------
# LOAD DATA
# ------------------------
df = pd.read_csv("data/cleaned_poll_data.csv")

# ------------------------
# SAFE SENTIMENT
# ------------------------
if "Sentiment" not in df.columns:
    def get_sentiment(text):
        return TextBlob(str(text)).sentiment.polarity
    df["Sentiment"] = df["Feedback"].apply(get_sentiment)

# ------------------------
# TITLE
# ------------------------
st.title("📊 Poll Results Visualizer - Advanced")

# ------------------------
# FILTERS
# ------------------------
colf1, colf2 = st.columns(2)

with colf1:
    region = st.selectbox("Select Region", df["Region"].unique())

with colf2:
    gender = st.selectbox("Select Gender", df["Gender"].unique())

filtered = df[(df["Region"] == region) & (df["Gender"] == gender)]

# ------------------------
# EMPTY CHECK
# ------------------------
if filtered.empty:
    st.warning("No data available for selected filters")
    st.stop()

# ------------------------
# KPI METRICS
# ------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered))
col2.metric("Avg Satisfaction", round(filtered["Satisfaction"].mean(), 2))
col3.metric("Top Tool", filtered["Preferred_Tool"].mode()[0])

# ------------------------
# BAR CHART
# ------------------------
st.subheader("📊 Tool Preference")

fig = px.bar(
    filtered,
    x="Preferred_Tool",
    color="Preferred_Tool",
    title="Tool Preference by Region & Gender"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# PIE CHART
# ------------------------
st.subheader("📊 Distribution")

fig2 = px.pie(
    filtered,
    names="Preferred_Tool",
    title="Tool Share"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------
# TIME SERIES ANALYSIS (FIXED)
# ------------------------
if "Timestamp" in df.columns:

    # Work on copy (safe)
    temp = filtered.copy()

    temp["Timestamp"] = pd.to_datetime(temp["Timestamp"])
    temp["Date"] = temp["Timestamp"].dt.date

    st.subheader("📈 Responses Over Time")

    daily = temp.groupby("Date").size().reset_index(name="count")

    fig3 = px.line(
        daily,
        x="Date",
        y="count",
        title="Daily Responses Trend"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ------------------------
# SENTIMENT ANALYSIS
# ------------------------
st.subheader("🧠 Sentiment Analysis")

avg_sentiment = filtered["Sentiment"].mean()

if avg_sentiment > 0:
    st.success(f"😊 Positive Sentiment ({avg_sentiment:.2f})")
elif avg_sentiment < 0:
    st.error(f"😡 Negative Sentiment ({avg_sentiment:.2f})")
else:
    st.warning(f"😐 Neutral Sentiment ({avg_sentiment:.2f})")

# ------------------------
# WORD CLOUD
# ------------------------
st.subheader("☁️ Feedback Word Cloud")

text = " ".join(filtered["Feedback"].astype(str))

if text.strip():
    wc = WordCloud(background_color="white").generate(text)

    fig_wc, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")

    st.pyplot(fig_wc)
else:
    st.write("No feedback available")

# ------------------------
# SMART INSIGHTS
# ------------------------
st.subheader("📌 Smart Insights")

top_tool = filtered["Preferred_Tool"].value_counts().idxmax()
least_tool = filtered["Preferred_Tool"].value_counts().idxmin()

st.write(f"👉 Most preferred tool: **{top_tool}**")
st.write(f"👉 Least preferred tool: **{least_tool}**")

avg_sat = filtered["Satisfaction"].mean()
st.write(f"👉 Average satisfaction score: **{avg_sat:.2f}**")

positive_ratio = (filtered["Sentiment"] > 0).mean() * 100
st.write(f"👉 {positive_ratio:.1f}% users gave positive feedback")

# ------------------------
# DOWNLOAD BUTTON
# ------------------------
st.subheader("📥 Download Data")

csv = filtered.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name='filtered_poll_data.csv',
    mime='text/csv',
)