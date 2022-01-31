#!/usr/bin/env python
# coding: utf-8

# ## Code and Resources

# We have analysed the dataset using python. The dataset that we have taken can contains Information about movies, Tv shows ,documentaries that are owned by NETFLIX Platform . We have done EDA and Data Visualization for NETFLIX Data.

# #   Importing python Libraries - numpy,panda,matplotlib,seaborn
# 

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

sns.set_style("darkgrid")
matplotlib.rcParams["font.size"] = 14
matplotlib.rcParams["figure.facecolor"] = '#00000000'


# ## Reading Data from dataset

# In[ ]:


netflix_data=pd.read_excel("netflix1.xlsx")
netflix_data


# ##  Converting data into Dataframe for our convenience 

# In[ ]:


netflix_df =pd.DataFrame(netflix_data)
netflix_df


# ## To know shape of Dataset

# In[ ]:


netflix_df.shape


# ## To view first 5  rows 

# In[ ]:


netflix_df.head(5)


# ## To view last 5 rows

# In[ ]:


netflix_df.tail(5)


# ## Displaying The Information of our Dataset

# In[ ]:


netflix_df.info()


# ## To determine dimension of dataset

# In[ ]:


netflix_df.ndim


# ## To check Null values in our dataset

# In[ ]:


netflix_df.isnull()


# ## To display total no.of null values

# In[ ]:


netflix_df.isnull().sum()


# ## To display sum of duplicates

# In[ ]:


netflix_df.duplicated().sum()


# ## To display Column names

# In[ ]:


netflix_df.columns


# ## To display top 30 rows of basic info for a movie or a TV show

# In[ ]:


netflix_df[['title','cast','country','description']].head(30)


# ## To Display different movies and Tv shows details in Netflix of Top 15 data

# In[ ]:


netflix_df[['title','type','country','release_year','duration','listed_in']].head(15)


# ### Data cleaning

# In[ ]:


#Handling missing value
netflix_df.director.fillna("No Director", inplace=True)
netflix_df.cast.fillna("No Cast", inplace=True)
netflix_df.country.fillna("Country Unavailable", inplace=True)
netflix_df.dropna(subset=["date_added", "rating"], inplace=True)


# # <font color=blue> Data Visualization </font>

# # Netflix Content By Type

# In[ ]:


plt.figure(figsize=(12,6))
plt.title("Percentage of Netflix Titles that are either Movies or TV Shows",fontsize=25, fontweight='bold')
g = plt.pie(netflix_df.type.value_counts(),explode=(0.05,0.05), labels=netflix_df.type.value_counts().index, colors=['blue','yellow'],autopct='%1.1f%%', startangle=180,shadow=True)
plt.show()


# # Countries by the Amount that Produces Content

# In[ ]:


filtered_countries = netflix_df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
filtered_countries = filtered_countries[filtered_countries != 'Country Unavailable']
plt.figure(figsize=(13,7))
g = sns.countplot(y = filtered_countries, order=filtered_countries.value_counts().index[:30])
plt.title('Top 30 Countries Contributor on Netflix')
plt.xlabel('Titles')
plt.ylabel('Country')
plt.show()


# # Top Directors on Netflix

# In[ ]:


filtered_directors = netflix_df[netflix_df.director != 'No Director'].set_index('title').director.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 15 Director Based on The Number of Titles')
sns.countplot(y = filtered_directors, order=filtered_directors.value_counts().index[:15], palette='Reds')
plt.show()


# # Top Genres on Netflix

# In[ ]:


filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
plt.figure(figsize=(10,10))
g = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:25])
plt.title('Top 25 Genres on Netflix')
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.show()


# # Top actor movies in Netflix

# In[ ]:


filtered_cast_movie = netflix_df[netflix_df.cast != 'No Cast'].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 25 Actor Movies Based on The Number of Titles')
sns.countplot(y = filtered_cast_movie, order=filtered_cast_movie.value_counts().index[:25], palette='pastel')
plt.show()


# # <font color=green> Summary </font>

# ### 1.The most content type on Netflix is movies,
# ### 2.The country by the amount of the produces content is the United States,
# ### 3.The most popular director on Netflix , with the most titles, is Jan Suter.
# ### 4.International Movies is a genre that is mostly in Netflix,
# ### 5.The most popular actor on Netflix movie, based on the number of titles, is Anupam Kher.
# 
