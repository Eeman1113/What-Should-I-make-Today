# -*- coding: utf-8 -*-
"""WHAT_SHOULD_I_MAKE_TODAY.ipynb

Original file is located at
    https://colab.research.google.com/drive/1bH3z8nvwSYUUX58m8UUDwzxNIvXhNTk6
"""

import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_Indian_dishes"
table_class="wikitable sortable  jquery-tablesorter"
table_classb="wikitable sortable north jquery-tablesorter"
table_classc="wikitable sortable south jquery-tablesorter"
table_classd="wikitable sortable west jquery-tablesorter"
table_classe="wikitable sortable east jquery-tablesorter"

response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
indiatable_a=soup.find('table',{'class':"wikitable sortable north"})
indiatable_b=soup.find('table',{'class':"wikitable sortable south"})
indiatable_c=soup.find('table',{'class':"wikitable sortable east"})
indiatable_d=soup.find('table',{'class':"wikitable sortable west"})
indiatable 
indiatable_a
indiatable_b
indiatable_c
indiatable_d

df=pd.read_html(str(indiatable))
df_a=pd.read_html(str(indiatable_a))
df_b=pd.read_html(str(indiatable_b))
df_c=pd.read_html(str(indiatable_c))
df_d=pd.read_html(str(indiatable_d))
# convert list to dataframe
df=pd.DataFrame(df[0])
df_a=pd.DataFrame(df_a[0])
df_b=pd.DataFrame(df_b[0])
df_c=pd.DataFrame(df_c[0])
df_d=pd.DataFrame(df_d[0])
print(df.head())
print(df_a.head(n=90))
print(df_b.head(n=66))
print(df_c.head(n=61))
print(df_d.head(n=93))

# drop the unwanted columns
data = df.drop(["Image", "Description"], axis=1)
data.head()

data_a = df_a.drop(["Image", "Description"], axis=1)
data_a.head(90)

data_b = df_b.drop(["Image", "Description"], axis=1)
data_b.head(66)

data_c = df_c.drop(["Image", "Description"], axis=1)
data_c.head(61)

data_d = df_d.drop(["Image", "Description"], axis=1)
data_d.head(93)

frames = [data,data_a, data_b, data_c,data_d]
result = pd.concat(frames)
result.reset_index(level=None, drop=True, inplace=True, col_level=0, col_fill='')
result.head(314)

result.to_csv('Food_of_India_Dataset.csv', index=1)
#https://www.kaggle.com/eemanmajumder/list-of-indian-food/