# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

df = pd.read_csv('datasets/insurance_claims.csv')
print(df.head(10))
print(df.shape)
print(df.nunique())
print(df['fraud_reported'].value_counts())


sns.countplot(x='incident_state', hue='incident_state', data=df)
plt.show()

table = pd.crosstab(df.age, df.fraud_reported)
print(table)
table.plot(kind='bar', stacked=True)
plt.show()

# feature engineering

df['fraud_reported'].replace(to_replace='Y', value=1,inplace = True)
df['fraud_reported'].replace(to_replace='N', value=0,inplace = True)

print(df.nunique())
df['csl_per_person'] = df.policy_csl.str.split('/', expand=True)[0]
df['csl_per_accident'] = df.policy_csl.str.split('/', expand=True)[1]

df['vehicle_age'] = 2020 - df['auto_year']

# categorising the hours into certain buckets
bins = [-1, 3, 6, 9, 12, 17, 20, 24]
names = ['past midnight', 'early_morning', 'morning', 'fore_noon', 'aftenoon', 'evening', 'night']
df['incident_period_of_day'] = pd.cut(df['incident_hour_of_the_day'],bins, labels=names).astype(object)

print(df[['incident_period_of_day','incident_hour_of_the_day']].head(10))

df.select_dtypes(include=['object']).columns

# removing columns that has no relavance 
df = df.drop(columns = ['policy_number',
                        'policy_csl',
                        'insured_zip',
                        'policy_bind_date',
                        'incident_date',
                        'incident_location',
                        '_c39',
                        'auto_year',
                        'incident_hour_of_the_day'])

print(df.head(2))

unknio

