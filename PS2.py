#!/usr/bin/env python
# coding: utf-8

# In[10]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PS2[dhimas]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM biodata1;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[17]:


import mysql.connector
import pandas as pd

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PS2[dhimas]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM biodata1;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Mengonversi hasil kueri ke DataFrame Pandas
    df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
    df_filtered = df[df['Gender'] == 'L']
    
    # Menampilkan hasil filter
    print("\nHasil Filter:")
    print(df_filtered)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[ ]:




