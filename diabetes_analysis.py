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
# %%
#找出年龄超过 40 岁且 BMI 大于 30 的患者，并按血糖值降序排列
diabetes_data_set[diabetes_data_set["BMI"]>30].sort_values(by="BMI",ascending=False)

# %%
#计算 Glucose 的均值、中位数、标准差和四分位距，判断分布是否偏态
gluc=diabetes_data_set["Glucose"]
print(gluc.mean(),"\n",gluc.median(),"\n",gluc.std(),"\n",gluc.quantile(0.75)-gluc.quantile(0.25),
      sep="")
skew=gluc.skew()
if abs(skew)>0.5:
    print("data of blood glucose level is skewed.")
else:
    print("data of blood glucose is approximately symmetric")
    
# %%
#group by Outcome，compare the average age, BMI and glucose level of patients in these two groups
columns2=["Age","BMI","Glucose"]
grouped_outcome=diabetes_data_set.groupby("Outcome")
print(grouped_outcome[columns2].agg(["mean", "median", "std"]))

#we can seperately get the cor.
for i in columns2:
    print(diabetes_data_set[i].corr(diabetes_data_set["Outcome"]))
    
#or together, with parameter names
print(diabetes_data_set[columns2+["Outcome"]].corr()["Outcome"])

# %%
#calculate correlation coefficient between Age, BMI and Glucose, explain the result
print(diabetes_data_set[columns2].corr())
#gluc has weak positive correlation with both age and BMI. 
#while the positive correlation between age and BMI is very weak

# %%
#group the patients by different age and compare the diabetes-positive proportion.
diabetes_data_set["Age_group"] = pd.cut(
    diabetes_data_set["Age"],
    bins=[20, 30, 40, 50, 60, 100],
    right=False)
positive_rate = diabetes_data_set.groupby(
    "Age_group",
    observed=True)["Outcome"].mean() * 100

print(positive_rate)

import matplotlib.pyplot as plt

positive_rate.plot(kind="bar")

plt.xlabel("Age group")
plt.ylabel("Diabetes positive rate (%)")
plt.title("Diabetes Positive Rate by Age Group")

plt.show()

# %%
#calculate positive proportion without using pd.cut
a=0
b=0
c=0
d=0
e=0
f=0
for i in diabetes_data_set["Age"]:
    if 30>i>=20:
        a+=1
    elif 40>i>=30:
        b+=1
    elif 50>i>=40:
        c+=1
posi_patient=diabetes_data_set[diabetes_data_set["Outcome"]==1]
for i in posi_patient["Age"]:
    if 30>i>=20:
        d+=1
    elif 40>i>=30:
        e+=1
    elif 50>i>=40:
        f+=1
print(d/a if a!=0 else None,"\n",e/b if b!=0 else None,"\n",f/c if c!=0 else None,sep="")

# %%
#calculate positive proportion without using pd.cut
a=0
b=0
c=0
d=0
e=0
f=0
for age,out in zip(diabetes_data_set["Age"],diabetes_data_set["Outcome"]):
    if 30>age>=20:
        a+=1
        if out==1:
            d+=1
    elif 40>age>=30:
        b+=1
        if out==1:
            e+=1
    elif 50>age>=40:
        c+=1
        if out==1:
            f+=1
print(d/a if a!=0 else None,"\n",e/b if b!=0 else None,"\n",f/c if c!=0 else None,sep="")







      


      








