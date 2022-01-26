#!/usr/bin/env python
# coding: utf-8

#                                                                                                         EXCLAMATORY DATA ANALYSIS OF NETFLIX DATA

# Importing python Libraries - numpy,panda,matplotlib,seaborn

# In[2]:


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


# Reading Data from dataset

# In[3]:


netflix_data=pd.read_excel("netflix1.xlsx")
netflix_data


# Converting data into Dataframe for our convenience

# In[4]:


netflix_df =pd.DataFrame(netflix_data)
netflix_df


# To know No.of Rows and Columns in Dataset

# In[5]:


netflix_df.shape


# To view top 5  rows 

# In[6]:


netflix_df.head(5)


# To view bottom 5 rows

# In[7]:


netflix_df.tail(5)


# Displaying The Information of our Dataset

# In[8]:


netflix_df.info()


# To determine dimension of dataset

# In[9]:


netflix_df.ndim


# To check Null values in our dataset

# In[10]:


netflix_df.isnull()


# To display total no.of null values

# In[11]:


netflix_df.isnull().sum()


# To display sum of duplicates

# In[39]:


netflix_df.duplicated().sum()


# To display Column names

# In[12]:


netflix_df.columns


# To display top 30 rows of basic info for a movie or a TV show

# In[36]:


netflix_df[['title','cast','country','description']].head(30)


# Data cleaning

# In[14]:


#Handling missing value
netflix_df.director.fillna("No Director", inplace=True)
netflix_df.cast.fillna("No Cast", inplace=True)
netflix_df.country.fillna("Country Unavailable", inplace=True)
netflix_df.dropna(subset=["date_added", "rating"], inplace=True)


# 1. Netflix Content By Type

# In[45]:


plt.figure(figsize=(13,7))
plt.title("Percentation of Netflix Titles that are either Movies or TV Shows")
g = plt.pie(netflix_df.type.value_counts(), labels=netflix_df.type.value_counts().index, colors=['red','yellow'],autopct='%1.1f%%', startangle=120)
plt.show()


# 2.Countries by the Amount that Produces Content

# In[16]:


filtered_countries = netflix_df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
filtered_countries = filtered_countries[filtered_countries != 'Country Unavailable']
plt.figure(figsize=(13,7))
g = sns.countplot(y = filtered_countries, order=filtered_countries.value_counts().index[:30])
plt.title('Top 30 Countries Contributor on Netflix')
plt.xlabel('Titles')
plt.ylabel('Country')
plt.show()


# 3. Top Directors on Netflix

# In[17]:


filtered_directors = netflix_df[netflix_df.director != 'No Director'].set_index('title').director.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 15 Director Based on The Number of Titles')
sns.countplot(y = filtered_directors, order=filtered_directors.value_counts().index[:15], palette='Reds')
plt.show()


# 4.Top Genres on Netflix

# In[18]:


filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
plt.figure(figsize=(10,10))
g = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:25])
plt.title('Top 25 Genres on Netflix')
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.show()


# 5.Top Actor TV Shows on Netflix

# In[33]:


filtered_cast_shows = netflix_df[netflix_df.cast != 'No Cast'].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 20 Actor TV Shows Based on The Number of Titles')
sns.countplot(y = filtered_cast_shows, order=filtered_cast_shows.value_counts().index[:20], palette='pastel')
plt.show()


# 6.top actor movies

# In[34]:


filtered_cast_movie = netflix_df[netflix_df.cast != 'No Cast'].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 25 Actor Movies Based on The Number of Titles')
sns.countplot(y = filtered_cast_movie, order=filtered_cast_movie.value_counts().index[:25], palette='pastel')
plt.show()

