#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
# Membuat dataframe dari data yang disalin ke clipboard
df = pd.read_clipboard()

# menampilkan dataframe
print(df)


# In[12]:


df


# In[13]:


# menghitung rata-rata tinggi
rata_tinggi = df['TB'].mean()
rata_tinggi


# In[14]:


print(df.dtypes)


# In[18]:


df['ANGKATAN'] = df['ANGKATAN'].astype(str)


# In[19]:


print(df.dtypes)


# In[20]:


df = pd.read_csv("C:/FILECSV/data_bioprak_new.csv")
df


# In[3]:


import pandas as pd

df = pd.read_excel("C:\FILECSV\data_bioprak_new.xlsx")
df


# In[10]:


import pandas as pd

data_nama = pd.read_csv("C:/FILECSV/data_bioprak_new.csv")


# In[ ]:





# In[ ]:




