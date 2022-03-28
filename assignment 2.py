#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


data = pd.read_csv("pokemon.csv")
data.head()


# In[10]:


data["Speed"].mean


# In[22]:


speed_mean = data["Speed"].mean()
def set_Speed(val):
    if val < speed_mean:
        return "Speed Low"
    elif val == speed_mean:
        return "Speed neutral"
    else:
        return "Speed High"


# In[23]:


data["Speed_high_low"] = data["Speed"].apply(set_Speed)
data


# In[ ]:




