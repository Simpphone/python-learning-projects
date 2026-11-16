# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:17:50 2026

@author: 18396
"""

import pandas as pd
diabetes_data_set=pd.read_csv(r"C:\Users\18396\Desktop\python\csv data set\diabetes.csv")
gluc=diabetes_data_set["Glucose"]
print(diabetes_data_set.columns)
# %%
#行选择
#indexed.df=df.set_index("ID")
patient_num_1=diabetes_data_set.loc[1]
print(patient_num_1)
print(patient_num_1==diabetes_data_set.iloc[1])


# %%
#相关分析
columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
columns_selected=diabetes_data_set[columns]
print(columns_selected.corr())

# %%
#单特征分群
grouped_glu=diabetes_data_set.groupby("Glucose")
print(grouped_glu["Age"].mean())

# %%
#多特征分群
pivot_table=diabetes_data_set.pivot_table(
    index="Age",
    columns="Outcome",
    values="Glucose",
    aggfunc="mean")
print(pivot_table)


      


      








