# -*- coding: utf-8 -*-
"""Market basket analysis_clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SP_JKktQUHaIo7n6kgOwaYzIuZsVc878
"""



from google.colab import drive
drive.mount('/content/drive')

pip install apyori

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('/content/drive/MyDrive/MBA dataset.csv',header=None)

dataset.head()

"""# Converted into List"""

transactions=[]
for i in range(0,7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

transactions

"""# Calculations"""

!pip install apyori
from apyori import apriori

Apriori_rules = apriori(transactions=transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2, max_length=2)
Results = list(Apriori_rules)

Results

"""# converting result list into tables"""

def inspect (Results):
  lhs = [tuple(result[2][0][0])[0] for result in Results]
  rhs = [tuple(result[2][0][1])[0] for result in Results]
  supports = [result[1] for result in Results]
  confidences = [result[2][0][2] for result in Results]
  lifts = [result[2][0][3] for result in Results]
  return list(zip(lhs, rhs, supports, confidences, lifts))
dataframe_final= pd.DataFrame(inspect(Results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

dataframe_final.head()

dataframe_final.nlargest(n=10, columns='Lift')