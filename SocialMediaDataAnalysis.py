#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[3]:


import pandas as pd                # For data manipulation and analysis
import numpy as np                 # For generating random numbers
import matplotlib.pyplot as plt    # For plotting graphs
import seaborn as sns              # For creating attractive statistical graphics
import random                      


# In[4]:


# Define categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health','Hollywood']


# In[5]:


# Create a random dataset of 10000 entries
n = 10000
data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}


# In[6]:


df = pd.DataFrame(data)


# In[7]:


print(df.head())


# In[8]:


print(df.info())
print(df.describe())


# In[9]:


print(df['Category'].value_counts())


# In[10]:


# Drop null and duplicate values if any
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


# In[11]:


# Convert 'Date' column to datetime and 'Likes' to integer

df['Date'] =pd.to_datetime(df['Date'])
df['Likes'] = df['Likes'].astype(int)


# In[15]:


#Histogram of Likes
plt.figure(figsize=(10,6))
sns.distplot(df['Likes'], bins=30, kde=True, hist=True, hist_kws={'edgecolor': 'black'})
plt.title("Distribution of Likes")
plt.xlabel("Number of Likes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# In[16]:


# Boxplot of Likes by Category
plt.figure(figsize=(12, 6))
sns.boxplot(x='Category', y='Likes', data=df)
plt.title("Likes by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[17]:


# Average number of Likes overall
print("\nOverall average Likes:", df['Likes'].mean())

# Average Likes per Category
print("\nAverage Likes per Category:")
print(df.groupby('Category')['Likes'].mean())


# In[18]:


# 1. Add a new column: Weekday
df['Weekday'] = df['Date'].dt.day_name()

# 2. Analyze average Likes by Weekday
avg_likes_by_weekday = df.groupby('Weekday')['Likes'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])


# In[19]:


# Plot: Average Likes by Weekday
plt.figure(figsize=(10, 5))
sns.barplot(x=avg_likes_by_weekday.index, y=avg_likes_by_weekday.values, palette="viridis")
plt.title("Average Likes by Weekday")
plt.xlabel("Day of the Week")
plt.ylabel("Average Likes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[20]:


# 3. Time Series Trend: Likes over Time (Rolling Average)
df_sorted = df.sort_values("Date")
df_sorted['Likes_Rolling'] = df_sorted['Likes'].rolling(window=14).mean()


# In[21]:


# Plot: Likes Rolling Average over Time
plt.figure(figsize=(12, 6))
plt.plot(df_sorted['Date'], df_sorted['Likes_Rolling'], color='darkorange')
plt.title("14-Day Rolling Average of Likes Over Time")
plt.xlabel("Date")
plt.ylabel("Rolling Avg Likes")
plt.tight_layout()
plt.show()


# In[30]:


# 4. Category performance over time (Line chart of category-level rolling means)
plt.figure(figsize=(12, 6))
for cat in df['Category'].unique():
    cat_df = df_sorted[df_sorted['Category'] == cat]
    rolling = cat_df.set_index('Date')['Likes'].rolling(window=600).mean()
    plt.plot(rolling, label=cat)


# In[31]:


# 5. Heatmap: Average Likes by Category and Weekday
pivot = df.pivot_table(index='Category', columns='Weekday', values='Likes', aggfunc='mean').reindex(
    columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Average Likes by Category and Weekday")
plt.xlabel("Weekday")
plt.ylabel("Category")
plt.tight_layout()
plt.show()


# In[32]:


# 6. Engagement score (create a normalized score for better comparisons)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['Engagement_Score'] = scaler.fit_transform(df[['Likes']])

# Average engagement score by category
print("\nAverage Engagement Score by Category:")
print(df.groupby('Category')['Engagement_Score'].mean().sort_values(ascending=False))


# In[ ]:




