# 📊 Social Media Data Analysis

This project simulates the work of a **Social Media Analyst** tasked with analyzing post engagement across various categories such as Food, Travel, Fashion, Fitness, Music, Culture, Family, and Health. The goal is to generate insights from randomly simulated data using Python, and present key visualizations and recommendations to optimize social media strategy.

---

## 🧠 Project Objectives

- Analyze the performance of different categories of social media posts.
- Visualize key engagement trends across time and categories.
- Provide data-driven insights and recommendations for improving content strategy.
- Showcase data analysis, feature engineering, and visualization skills for BI and data analyst roles.

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas** – for data manipulation
- **NumPy** – for numerical operations
- **Matplotlib** – for plotting static visualizations
- **Seaborn** – for attractive statistical plots
- **scikit-learn** – for engagement score normalization (MinMaxScaler)
- **Random** – for simulating category assignment

---

## 📁 File Structure

- `SocialMediaDataAnalysis.py`: Python script containing the complete workflow – data generation, cleaning, analysis, and visualization.
- `README.md`: Documentation for project overview and instructions.

---

## 📈 Key Analyses Performed

### 1. **Data Simulation**
- Randomly generated 500 social media posts.
- Simulated categories, post dates, and number of likes.

### 2. **Data Cleaning**
- Removed nulls and duplicates.
- Converted date to datetime format and likes to integers.

### 3. **Visualizations**
- **Histogram** of likes distribution with bin edges.
- **Boxplot** of likes across categories.
- **Bar chart** of average likes by weekday.
- **Line chart** showing 14-day rolling average of likes.
- **Multi-line trend** for category-wise performance over time.
- **Heatmap** of average likes by category and weekday.

### 4. **Advanced Analysis**
- Extracted weekday as a new feature.
- Created a normalized **Engagement Score** using MinMaxScaler.
- Ranked categories based on average engagement.

---

## 📌 Insights & Recommendations

- Certain categories (e.g., *Culture*, *Travel*) tend to receive more engagement.
- Optimal posting days vary by category (e.g., *Fitness* performs better on weekends).
- Rolling averages help identify consistent engagement trends.

---

## 💡 Future Improvements

- Replace synthetic data with real Twitter API data via Tweepy or snscrape.
- Incorporate NLP-based sentiment analysis (TextBlob, VADER).
- Add post time and content-based features (hashtags, length, etc.).
- Build an interactive dashboard using Plotly Dash or Streamlit.

---

## 👤 Author

**Rhea George**  
🔗 [LinkedIn](https://www.linkedin.com/in/rheageorge99/)


