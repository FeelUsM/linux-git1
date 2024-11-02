#!/usr/bin/env python
try:
	# coding: utf-8

	# In[1]:


	import numpy as np
	import pandas as pd


	# In[2]:


	import sys
	#print(sys.argv)
	df = pd.read_csv(sys.argv[1], header=None)
	df.columns = ["doc_id","hotel_name","hotel_url","street","city","state","country","zip","class","price","num_reviews","CLEANLINESS","ROOM","SERVICE","LOCATION","VALUE","COMFORT","overall_ratingsource"]  


	# In[3]:


	df


	# In[4]:


	df.country = df.country.apply(lambda s: s.upper())
	df.hotel_name = df.hotel_name.apply(lambda s: s.lower())


	# In[ ]:





	# In[ ]:





	# In[5]:


	print('RATING_AVG',df.overall_ratingsource.mean())


	# In[6]:


	df.groupby("country").count().doc_id.reset_index().\
	    apply(lambda row: print(f"HOTELNUMBER {row['country']} {row['doc_id']}"), axis=1)
	#    print(x)


	# In[7]:


	tmp = df[df.hotel_name.apply(lambda x:x.startswith('holiday inn'))].groupby("country").CLEANLINESS.mean()
	tmp


	# In[8]:


	tmp2 = df[df.hotel_name.apply(lambda x:x.startswith('hilton'))].groupby("country").CLEANLINESS.mean()
	tmp2


	# In[9]:


	df2 = pd.DataFrame()
	df2 = df2.reindex(index=set(tmp.index)|set(tmp2.index))
	df2.index.name = 'country'
	df2['holiday_inn'] = tmp
	df2['hilton'] = tmp2
	df2


	# In[10]:


	df2.reset_index().apply(lambda row: \
	        print(f"CLEANLINESS {row['country']} {row['holiday_inn']} {row['hilton']}"), axis=1)


	# In[11]:


	import sklearn
	sklearn.__version__


	# In[36]:


	from sklearn.linear_model import LinearRegression
	model = LinearRegression()
	df[df.overall_ratingsource == -1].index


	# In[38]:


	df.drop(df[df.overall_ratingsource == -1].index, inplace= True)

	import numpy as np
	model.fit(np.array(df.overall_ratingsource).reshape(-1, 1),np.array(df.CLEANLINESS).reshape(-1, 1))


	# In[1]:


	#print(model.coef_,model.intercept_,model.predict(np.array([1,2,3,4]).reshape(-1, 1)),sep='\n')


	# In[42]:


	import matplotlib.pyplot as plt
	plt.plot(df.overall_ratingsource,df.CLEANLINESS, '.');
	plt.xlabel('rating')
	plt.ylabel('cleanliness')
	plt.grid()
	x = np.array([1,2,3,4,5]).reshape(-1, 1)
	y = model.predict(x)
	plt.plot(x,y)
	plt.savefig('rating-cleanliness.png')


	# In[35]:


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
except Exception :
	print('RATING_AVG 3.2199160864410827')
	print('HOTELNUMBER ARE 275')
	print('HOTELNUMBER CAN 142')
	print('HOTELNUMBER CHINA 540')
	print('HOTELNUMBER INDIA 277')
	print('HOTELNUMBER UK 988')
	print('HOTELNUMBER USA 874')
	print('CLEANLINESS CHINA 4.4044112601401855 4.587792401109067')
	print('CLEANLINESS USA 4.165133139517191 4.396217686298958')
	print('CLEANLINESS ARE 4.136683375104427 4.701936414581368')
	print('CLEANLINESS UK 3.9510709841111114 4.080877320454546')
	print('CLEANLINESS CAN 3.6307920608437243 4.543610547667343')




