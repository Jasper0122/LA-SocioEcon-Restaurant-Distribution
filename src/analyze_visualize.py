"""
Analyze Visualize

Author: <Zongrong Li 3707497945 DSCI 510>
"""
import seaborn as sns
import pandas as pd
import folium
from folium.plugins import HeatMap
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the data
file_path = '../data/processed/integrated_data.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataframe
df_info = df.info()
df_head = df.head()

df_info, df_head

# Group the data by 'ADI_NATRANK_Category' and get the counts for each 'Review_num', 'Rating', and 'Price'
review_num_counts = df.groupby('ADI_NATRANK_Category')['Review_num'].value_counts().rename('count').reset_index()
rating_counts = df.groupby('ADI_NATRANK_Category')['Rating'].value_counts().rename('count').reset_index()
price_counts = df.groupby('ADI_NATRANK_Category')['Price'].value_counts().rename('count').reset_index()

# Function to create bar plots
def create_bar_plot(data, x, y, hue, title, ax):
    sns.barplot(x=x, y=y, hue=hue, data=data, ax=ax)
    ax.set_title(title)
    ax.set_xlabel('ADI_NATRANK_Category')
    ax.set_ylabel('Count')

# Set up the matplotlib figure
fig, axes = plt.subplots(1, 3, figsize=(21, 7), constrained_layout=True)  # Change from 3, 1 to 1, 3 and adjust figsize

# Create a bar plot for 'Review_num' within each 'ADI_NATRANK_Category'
create_bar_plot(review_num_counts, 'ADI_NATRANK_Category', 'count', 'Review_num', 'Count of Review Numbers by ADI National Rank Category', axes[0])

# Create a bar plot for 'Rating' within each 'ADI_NATRANK_Category'
create_bar_plot(rating_counts, 'ADI_NATRANK_Category', 'count', 'Rating', 'Count of Ratings by ADI National Rank Category', axes[1])

# Create a bar plot for 'Price' within each 'ADI_NATRANK_Category'
create_bar_plot(price_counts, 'ADI_NATRANK_Category', 'count', 'Price', 'Count of Prices by ADI National Rank Category', axes[2])

plt.show()

# Calculate correlations between numeric features
correlation_matrix = df[['Review_num', 'Rating', 'Price']].corr()

# Set up the matplotlib figure
plt.figure(figsize=(9, 8))

# Draw the heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5)

# Show the plot
plt.show()


# Function to generate word clouds for each category
def generate_wordclouds(df, category_col, text_col):
    categories = df[category_col].unique()
    wordclouds = {}
    for cat in categories:
        # Combine text from the same category
        text = ' '.join(df[df[category_col] == cat][text_col].dropna().values)
        if text:  # Check if text is not empty
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            wordclouds[cat] = wordcloud
    return wordclouds

# Generate word clouds for each ADI_NATRANK_Category in the 'Categories' column
wordclouds_by_adi_category = generate_wordclouds(df, 'ADI_NATRANK_Category', 'Categories')

# Number of categories
num_categories = len(wordclouds_by_adi_category)

# Set up the matplotlib figure
fig, axes = plt.subplots(nrows=1, ncols=num_categories, figsize=(num_categories*8, 8))  # Adjust subplot to 1 row and as many columns as there are categories

# If there is only one category, axes will not be an array, so we need to check and wrap it in a list if necessary
if not isinstance(axes, np.ndarray):
    axes = [axes]

# Display the word clouds side by side
for ax, (cat, wordcloud) in zip(axes, wordclouds_by_adi_category.items()):
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_title(f'ADI_NATRANK_Category {cat}')
    ax.axis('off')

plt.tight_layout()
plt.show()



