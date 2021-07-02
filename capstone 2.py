#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt

import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
sns.set_style('darkgrid')
mpl.rcParams['figure.figsize']=(20,5)
import csv


# In[21]:


df=pd.read_csv('C:\\Users\danzengy\Southern\hotel_bookings.csv')
df.head()
df.info()


# In[69]:


data.hist(figsize=(20,15))
plt.show()


# In[73]:


sns.boxplot(x='children',y='company',data=df)
plt.figure(figsize=(20, 10))

index = 0
for i in ['adults', 'children', 'babies']:
    index += 1
    plt.subplot(2, 3, index)
    plt.plot(df.groupby(i)['is_canceled'].mean(),
             'ro-',
             ms=4)
    plt.title(people)

    plt.subplot(2, 3, index + 3)
    i_stats = df[i].value_counts()
    sns.barplot(x=i_stats.index, y=i_stats.values)
plt.tight_layout()
plt.show()


# In[ ]:


INSIGHT: Having one child is the most common amount of kids hotel see


# In[14]:





# In[22]:


sns.countplot(x=df['hotel'], hue=df['is_canceled'])
plt.show()


# In[ ]:


Insight: we can see that hotel cancellations is pretty common and that more than half of the hotels reserverd in the city are cancelled.


# In[77]:


index = 1
for room in ['reserved_room_type', 'assigned_room_type']:
    ax1 = plt.subplot(2, 1, index)
    ax2 = ax1.twinx()
    ax1.bar(
        df.groupby(room).size().index,
        df.groupby(room).size())
    ax1.set_xlabel(room)
    ax1.set_ylabel('Number')
    ax2.plot(
        df.groupby(room)['is_canceled'].mean(),'ro-')
    ax2.set_ylabel('Cancellation rate')
    plt.show()


# In[ ]:


InsightL: we can see that the most common type of rooms reserved are A and D and that they both have around 50% cancellation rate


# In[64]:


season = df.groupby("arrival_date_month")["hotel"].count()
months = season.index


sns.barplot(x=months, y=season)
plt.xlabel("Months")
plt.ylabel("Number of guests")

plt.show()

plt.figure(figsize=(12,6))
sns.countplot(data=df , x='arrival_date_month', hue='hotel')


# In[ ]:





# In[ ]:


Insight: august is the most popular month and 


# In[55]:



plt.figure(figsize=(20,10))
plt.xlim(0, 1000)
plt.ylim(0, 450)
sns.boxplot(x='reserved_room_type',y='adr',hue='hotel',data=df)
plt.xlabel('Rooms Reserved')
plt.ylabel('Price')
plt.tight_layout()
plt.show()


# In[ ]:


Insight: we can see the highs and lows for each type of room for both city and resort. Generally the resort rooms start lower and end lower but there are cases when the city hotel does that too.


# In[63]:


plt.figure(figsize=(20,10))
sns.lineplot(x='arrival_date_month', y='adr', hue='hotel', data= df)
plt.show()


# In[ ]:


Insight: we can see from this graph that the highest prices are in August and the lowest prices are in november and January


# In[79]:


plt.figure(figsize=(10,8))
sns.countplot(x='hotel',hue='arrival_date_year',data=df)


# In[ ]:




