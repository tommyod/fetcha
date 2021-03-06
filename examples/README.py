#!/usr/bin/env python
# coding: utf-8

# # fetcha
# 
# Talk to SSB using Python.

# ## Installation

# In[ ]:


pip install git+https://github.com/dafeda/fetcha.git --upgrade


# In[1]:


import fetcha as fetcha


# In[2]:


# Instantiate object with specific table_id that refers to a SSB-table.
# 10945 refers to Monetary aggregates M1, M2 and M3:
# https://www.ssb.no/en/statbank/table/10945
ssb_10945 = fetcha.SSB("10945", language="en")


# In[3]:


# Number of rows in table.
ssb_10945.nrows_tot()


# In[4]:


# Number of rows per period.
ssb_10945.nrows_period()


# In[5]:


# Get all available periods
periods = ssb_10945.periods()
periods[-7:]


# In[6]:


# Fetch latest period.
# Returns a pandas dataframe with its index set with verify_integrity set to True.
# If the dataframe is lacking an index, it means that the index columns do not make up a unique combination.
df_latest = ssb_10945.fetch()
df_latest.head()


# In[8]:


# Fetch list of periods
df_periods = ssb_10945.fetch(["2019M12", "2020M01", "2020M02"])
df_periods.head()


# In[9]:


# Fetch whole year of data
df_year = ssb_10945.fetch("2020")
df_year.head()


# In[10]:


# Fetch multiple years
df_years = ssb_10945.fetch(["2019", "2020"])
df_year.head()


# In[11]:


# Pivot helper function - a thin wrapper over pandas' pivot_table.
ssb_10945.pivot(df_year)


# In[12]:


# Fetch and join
# Get another table so we have something to join with.
ssb_10948 = fetcha.SSB("10948", language="en")
df_10948 = ssb_10948.pivot(ssb_10948.fetch("2020"))

df_10948.join(df_year)


# In[13]:


# Use id when pivoting for prettier column names.
df_10945_id = ssb_10945.pivot(ssb_10945.fetch(id_cols=True), "contents_id")


# In[14]:


df_10945_id.head()


# In[15]:


# SSB has a limit of 300k rows per transaction.
# Some tables have more than that in one period.
ssb_10261 = fetcha.SSB("10261", language="en")


# In[16]:


# Gives warning and returns None.
df_10261 = ssb_10261.fetch()


# In[17]:


# Can pass filter to fetch(), but first we need to choose what we want.
# Use variable levels to see which options you have.
ssb_10261.levels


# In[18]:


# We limit the region to "The whole country".
ssb_10261.levels.iloc[0]


# In[19]:


fltr = [{"code": "Region", "values": ["0"]}]


# In[20]:


df_10261 = ssb_10261.fetch(fltr=fltr)


# In[21]:


df_10261.shape


# In[22]:


df_10261.sample(10)


# In[ ]:




