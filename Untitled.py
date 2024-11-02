#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

# In[4]:


#df = pd.read_csv('/home/users/datasets/hotels.csv', header=None)
import sys
df = pd.read_csv(sys.argv[1], header=None)
df.columns = ["doc_id","hotel_name","hotel_url","street","city","state","country","zip","class","price","num_reviews","CLEANLINESS","ROOM","SERVICE","LOCATION","VALUE","COMFORT","overall_ratingsource"]  
df = df.replace(-1, np.nan)
df = df.replace('-1',np.nan)

# In[5]:


df

# In[7]:


#df.country = df.country.apply(lambda s: s.upper())
#df.hotel_name = df.hotel_name.apply(lambda s: s.lower())


# In[ ]:




# In[ ]:




# In[8]:


print('RATING_AVG',df.overall_ratingsource.mean())

# In[9]:


df.groupby("country").count().doc_id.reset_index().\
    apply(lambda row: print(f"HOTELNUMBER {row['country']} {row['doc_id']}"), axis=1)
#    print(x)

# In[10]:


tmp = df[df.hotel_name.apply(lambda x:x.startswith('holiday inn'))].groupby("country").CLEANLINESS.mean()
tmp

# In[11]:


tmp2 = df[df.hotel_name.apply(lambda x:x.startswith('hilton'))].groupby("country").CLEANLINESS.mean()
tmp2

# In[12]:


df2 = pd.DataFrame()
df2 = df2.reindex(index=set(tmp.index)|set(tmp2.index))
df2.index.name = 'country'
df2['holiday_inn'] = tmp
df2['hilton'] = tmp2
df2

# In[13]:


df2.reset_index().apply(lambda row: \
        print(f"CLEANLINESS {row['country']} {row['holiday_inn']} {row['hilton']}"), axis=1)

# In[14]:


import sklearn
sklearn.__version__

# In[20]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()


# In[23]:


df = df.drop(df[df.overall_ratingsource.isna()].index)
model.fit(np.array(df.overall_ratingsource).reshape(-1, 1),np.array(df.CLEANLINESS).reshape(-1, 1))

# In[24]:


#print(model.coef_,model.intercept_,model.predict(np.array([1,2,3,4]).reshape(-1, 1)),sep='\n')

# In[25]:


import matplotlib.pyplot as plt
plt.plot(df.overall_ratingsource,df.CLEANLINESS, '.');
plt.xlabel('rating')
plt.ylabel('cleanliness')
plt.grid()
x = np.array([1,2,3,4,5]).reshape(-1, 1)
y = model.predict(x)
plt.plot(x,y)
plt.savefig('rating-cleanliness.png')

# In[26]:


model.score(np.array(df.overall_ratingsource).reshape(-1, 1),np.array(df.CLEANLINESS).reshape(-1, 1), sample_weight=None)

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[22]:


from importlib.metadata import distributions

# In[23]:


sorted(x.name for x in distributions())
#    print(, x.locate_file('/'))

# In[17]:


dir(next(iter( distributions())))

# In[ ]:



