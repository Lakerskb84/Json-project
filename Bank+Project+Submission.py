
# coding: utf-8

# In[238]:


#Importing Pandas,json and json_normalize
import pandas as pd
import json
from pandas.io.json import json_normalize


# In[239]:


#changed data/world_bank_projects.json to 'world_bank'. Loaded 'world_bank' as a json file and normalized columns
# 'mjtheme_namecode' and 'countryname'
json_df=json.load((open('world_bank')))
json_normalize(json_df, 'mjtheme_namecode')
json_normalize(json_df, 'mjtheme_namecode', ['countryname'])


# In[240]:


#Changed json to a pandas DataFrame, json2_df then printed the  data frame
json2_df=pd.DataFrame(json_df)
print(json2_df)


# In[241]:


# Top 10 results for countries with projects
json2_df['countryname'].value_counts().head(10)


# In[242]:


# Normalized data frame using 'mjtheme_namecode'
projects=json_normalize(json_df, 'mjtheme_namecode')
print(projects)


# In[243]:


# Grouped projects by name using the number of projects and sorted the values in decending order
# listing the top 10 projects using .head(10)
projects.groupby('name').size().sort_values(ascending=False).head(10)


# In[244]:


# Dropped all duplicate names to determine which rows had NaN or empty 
# Values
missing= projects.fillna(0)
print(missing)


# In[245]:


#turned into a pandas data frame
final=pd.DataFrame(missing)
print(final)


# In[246]:


# Turned the column 'code' into an integer to be able to concatonate
# both columns then sort the values by 'code' so all missing values
# for 'name' would be together
a= missing[['code']].astype(int)
b= missing[['name']]
c=pd.concat([a,b], axis=1)
c=c.sort_values('code')
c=c.reset_index(drop= True)
print(c)


# In[248]:


# creating pandas df, result_df. 
result_df=pd.DataFrame(c)
print(result_df)

