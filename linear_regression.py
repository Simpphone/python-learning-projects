# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:27:46 2026

@author: 18396
"""
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as sts
import numpy as np
import pandas as pd
dm=pd.read_csv( r"C:\Users\18396\Desktop\python\csv data set\diamonds.txt")
columns1=dm.columns=['carat','cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']

# %%
#visual figures
print(sb.pairplot(dm[columns1]))
# %%
#visual figures
print(dm[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].corr()["price"])

# %%
#model training
import statsmodels.api as sm
Y=dm["price"]
X=sm.add_constant(dm["carat"])#add intercept
model=sm.OLS(Y, X)#ordinary least squares
result=model.fit()
print(result.summary())#focus on R square, p>t, coef
#p value here refers to H0: regression coefficient==0, reject that if p<0.05
# %%
#multiple regression
predictors=["carat","x"]

Y=dm["price"]
X=sm.add_constant(dm[predictors])#add intercept
model=sm.OLS(Y, X)#ordinary least squares
result=model.fit()
print(result.summary())
#multicollinearity
# %%

#categorical data processing
pd.get_dummies(dm["color"],drop_first=True,dtype=int)#turn cate. data into digital/quantitive data
predictors1=["carat","color"]
Y=dm["price"]
X=sm.add_constant(pd.get_dummies(dm[predictors1],columns=["color"],drop_first=True,dtype=int))#add intercept
model=sm.OLS(Y, X)#ordinary least squares
result=model.fit()
print(result.summary())

# %%
#also can test the model using existing data
predictors1=["carat","color"]
Y=dm["price"]
X=sm.add_constant(pd.get_dummies(dm[predictors1],columns=["color"],drop_first=True,dtype=int))#add intercept
X_train=X[1000:]
X_test=X[:1000]
Y_train=Y[1000:]
Y_test=Y[:1000]
model=sm.OLS(Y_train, X_train)#ordinary least squares
result=model.fit()
predicted=result.predict(X_test)
print(predicted.sample(10))
print(predicted.describe())

# %%
#model assessment
y_pre=predicted
y_act=Y_test
residuals=y_act-y_pre
MAE=residuals.abs().mean()




    


