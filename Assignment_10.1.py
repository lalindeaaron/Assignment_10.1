# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:17:06 2018

@author: Arron con Pollo
"""
import pandas as pd

#reading dataset & dropping unnamed column
df = pd.read_csv('US_Baby_Names_right.csv.txt', index_col=0)

#show distribution of male and female
a = df['Gender'].value_counts()
df['Gender'].value_counts().plot(title='Gender distribution',kind='bar')

#show top five most preferred names
print(df.groupby(['Name']).Name.value_counts().nlargest(5))

#median name occurance in the dataset
print(df.groupby(['Name']).Name.value_counts().mean())

#distribution of male and female born count by states
df.groupby(['Gender','State']).Gender.value_counts()

