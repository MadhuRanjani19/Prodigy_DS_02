# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CVHfHAFoiM8c5XFbqugt6qSvo74KAa39
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'/content/gender_submission.csv'
df = pd.read_csv(file_path)

print("Basic Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', palette='Set2')
plt.title('Survival Distribution')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(5,5))
df['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'], labels=['Did not survive', 'Survived'])
plt.title('Survival Rate')
plt.ylabel('')
plt.show()