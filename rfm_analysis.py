# -*- coding: utf-8 -*-
"""RFM_Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zOX7NkNpFat76NglKWqQhLG9YQCXuHJS

# RFM ANALYSIS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

data=pd.read_csv('/content/drive/MyDrive/rfm Analysis data (1).csv',encoding='unicode_escape')

from google.colab import drive
drive.mount('/content/drive')

da=data.copy()

da.head()

da.shape

da.isnull().sum()

da.dropna(inplace=True)

#how many unique items we have in data?
da['Description'].nunique()

da['Description'].value_counts()

#Rank five most ordered products
da.groupby('Description').aggregate({"Quantity":"sum"}).sort_values(by="Quantity",ascending=False).head(5)

da['Invoice'].value_counts()

da=da[~da['Invoice'].str.contains('C',na=False)]

#calculate total revenue
da['TotalPrice']=da['Quantity']*da['Price']

da['InvoiceDate']=pd.to_datetime(da['InvoiceDate'])

da['InvoiceDate'].max()

today_date=dt.datetime(2010,12,10)
rfm=da.groupby('Customer ID').agg({'InvoiceDate':lambda date:(today_date-date.max()).days,
                                   'Invoice':lambda num:num.nunique(),
                                   'TotalPrice':lambda TotalPrice:TotalPrice.sum()})
rfm.coloumns=['Recency','Frequency','Monetary']

rfm

today_date=dt.datetime(2010,12,10)
rfm=da.groupby('Customer ID').agg({'InvoiceDate':lambda date:(today_date-date.max()).days,
                                   'Invoice':lambda num:num.nunique(),
                                   'TotalPrice':lambda TotalPrice:TotalPrice.sum()})
rfm.columns=['Recency','Frequency','Monetary'] # Fixed typo: 'coloumns' to 'columns'
rfm["recency_score"]=pd.qcut(rfm['Recency'],5,labels=[5,4,3,2,1])

rfm["frequency_score"]=pd.qcut(rfm['Frequency'].rank(method='first'),5,labels=[1,2,3,4,5])
# Changed 'frequency' to 'Frequency' to match the existing column name

rfm["monetary_score"]=pd.qcut(rfm['Monetary'],5,labels=[1,2,3,4,5])

top_customers = rfm[(rfm['recency_score'].isin([4, 5])) &
                    (rfm['frequency_score'].isin([4, 5])) &
                    (rfm['monetary_score'].isin([4, 5]))].head(10)
print(top_customers)

rfm["rfm_score"]=rfm["recency_score"].astype(str)+rfm["frequency_score"].astype(str)+rfm["monetary_score"].astype(str)

rfm.head()

"""# create the different segment of customers"""

seg_map={
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'champions'
}
rfm['segment']=rfm['rfm_score'].replace(seg_map,regex=True)
rfm.head()

rfm[["segment","Recency","Frequency","Monetary"]].groupby("segment").agg(["count"]).round()