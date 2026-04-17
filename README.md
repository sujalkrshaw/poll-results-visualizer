# 📊 Poll Results Visualizer (Advanced)

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

### 🚀 A complete end-to-end data analytics project that transforms survey data into actionable insights using visualization and NLP.

---

## 🚀 Overview

The **Poll Results Visualizer** is an end-to-end data analytics project designed to process, analyze, and visualize survey/poll data using Python.

It converts raw survey responses into **interactive dashboards, meaningful insights, and visual reports**, enabling faster and smarter decision-making.

---

## 🎯 Problem Statement

Raw poll or survey data is:

* Difficult to interpret
* Time-consuming to analyze manually
* Not directly useful for decision-making

---

## 💡 Solution

This project builds a **complete analytics pipeline** that:

* Cleans and preprocesses poll data
* Performs statistical and sentiment analysis
* Generates interactive visualizations
* Provides actionable insights via a dashboard

---

## 🛠️ Tech Stack

* **Programming:** Python
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Dashboard:** Streamlit
* **NLP:** TextBlob (Sentiment Analysis)
* **Text Visualization:** WordCloud

---

## 📂 Project Structure

```
Poll-Results-Visualizer/
│
├── app/                # Streamlit dashboard
│   └── app.py
│
├── data/               # Dataset files
│   ├── raw_poll_data.csv
│   └── cleaned_poll_data.csv
│
├── src/                # Core modules
│   ├── data_generator.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── visualization.py
│   └── sentiment.py
│
├── outputs/            # Generated charts
├── images/             # Screenshots
├── requirements.txt
└── main.py
```

---

## ⚙️ Key Features

### 📌 Data Processing

* Synthetic poll data generation
* Data cleaning & preprocessing
* Feature engineering (Timestamp, Sentiment)

### 📊 Visualization

* Bar chart (Tool Preference)
* Pie chart (Distribution)
* Time-series trend analysis
* Word cloud (Feedback analysis)

### 🧠 Analytics

* Sentiment analysis on feedback
* KPI metrics:

  * Total responses
  * Average satisfaction
  * Top preferred tool
* Automated insight generation

### 🎛️ Interactive Dashboard

* Filters (Region, Gender)
* Dynamic visualizations
* Download filtered dataset option

---

## 📈 Key Insights

* Python is the most preferred tool (~40% share)
* Positive feedback rate is over 90%
* Average satisfaction score is approximately 3.2/5
* Noticeable variation across regions and demographics

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Generate Data

```bash
python main.py
```

### 3️⃣ Run Dashboard

```bash
streamlit run app/app.py
```

---

## 📸 Screenshots

### 📊 Dashboard

![Dashboard](images/dashboard.png)

### 📈 Charts

![Charts](images/charts.png)

### 🧠 Sentiment Analysis

![Sentiment](images/sentiment.png)

### ☁️ Word Cloud

![WordCloud](images/wordcloud.png)

---

## 🧠 Key Learnings

* End-to-end data pipeline development
* Data cleaning and preprocessing techniques
* Data visualization and dashboard design
* Sentiment analysis using NLP
* Real-world project structuring

---

## 🚀 Future Improvements

* Real-time poll integration (API)
* Advanced NLP (topic modeling, sentiment classification)
* Deployment on cloud (Streamlit Cloud / AWS)
* Power BI integration

---

## 📌 Impact

This project helps organizations quickly analyze feedback data and make informed, data-driven decisions.

---

## 💼 Resume Value

This project demonstrates:

* Data Analysis & Visualization
* Python Development
* Dashboard Creation
* Analytical Thinking & Problem Solving

---

## 👨‍💻 Author

**Sujal kumar  Shaw**

---

## ⭐ If you like this project, give it a star!
