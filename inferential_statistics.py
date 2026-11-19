# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:32:43 2026

@author: 18396
"""

import scipy.stats as sts
import numpy as np
import pandas as pd
dm=pd.read_csv( r"C:\Users\18396\Desktop\python\csv data set\diamonds.txt")
columns=dm.columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']

# %%

print(dm.describe())
# %%
#confidence intervals of price
n=dm["price"].count()
s=dm["price"].std()
xbar=dm["price"].mean()
conf=0.95

SEM=s/np.sqrt(n)

interval=sts.norm.interval(confidence=conf, loc=xbar, scale=SEM)
print("With 95% confidence, the mean of diamonds falls in",interval[0],"and",interval[1])

# %%

#single sample t-test
#H0: mean price of premium diamonds is above 4500
t,p=sts.ttest_1samp(
    dm[dm["cut"]=="Premium"]["price"],
    popmean=4500,
    alternative="greater" #oppositely, "less", or "two-sided"
)

if p>0.05:
    print("Insufficient evidence prove state ''mean price of premium diamonds is above 4500'' is wrong.")
else:
    print("sufficient evidence prove state ""mean price of premium diamonds is above 4500"" is wrong\ntherefore reject it, accept H1")

# %%

#double sample ttest
dst=sts.ttest_ind(dm[dm["cut"]=="Premium"]["price"],dm[dm["cut"]=="Fair"]["price"])
if dst[1]>0.05:
    print("Insufficient evidence to reject the null hypothesis that the mean prices of premium and fair diamonds are equal.")
else:
    print("Sufficient evidence to reject the null hypothesis that \"the mean prices of premium and fair diamonds are equal.\" is wrong\ntherefore reject it, accept H1")

# %%

#generate simulation samples
n1=1000#sample amount
uni_sp=np.random.uniform(low=0,high=0.1,size=n1)#uniform distri.
norm_sp=np.random.normal(scale=s,loc=xbar,size=n1)#normal


