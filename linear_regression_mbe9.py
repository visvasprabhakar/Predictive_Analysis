# -*- coding: utf-8 -*-
"""Linear Regression MBE9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zzNEKtdAXCYH7vBk4HeRg6UAky3aNp4U

# Google Play Store Predictions using Linear Regression

***Problem Statement:*** Whenever a new app is uploaded on Google play store, that app will be assigned by a predictive ratings.

# Steps to create ML model
1. Import Library
2. Import the dataset
3. Data pre-Processing
  

*   Data Cleaning
*   Understaning the Data

4. Convert the categorical data into numerical data
5. Extract Dependent variables(Targets) and Independent Variable(Features)
6. Separate the data into TRAIN and TEST
7. Applying Algorithm(Linear Regression)
8. Test the Algorithm

# STEP-1: Import Library
1. Pandas- Data Cleaning/Manupulatiion
2. Numpy- Manage Array
3. Matplotlib- Visualization
4. Seaborn- Advanced Analytical Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# Step-2: Import the data
1. Pandas library to import dataset
"""

data= pd.read_csv('/content/drive/MyDrive/googleplaystore.csv')

"""Understand Your dataset
1. head()
2. shape
3. info()
"""

data.head()

data.info()

data.isnull().sum()