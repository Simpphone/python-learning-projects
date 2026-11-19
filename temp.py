# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#使用 for 循环，计算每种药物的费用（单价 × 数量）。
#计算所有药物的总费用。
#如果总费用超过 £20，打印 "Over budget"，否则打印 "Within budget"。

drugs = ["Paracetamol", "Ibuprofen", "Amoxicillin"]
prices = [2.5, 4.0, 8.5]
quantities = [2, 1, 3]
total=0
for i in range(len(drugs)):
    cost=prices[i]*quantities[i]
    print(drugs[i],":",cost)
    total+=cost
print("Total",":",total)
if total>=20:
    print("Over budget")
else:
    print("Within budget")
# %%
#使用 for 循环遍历 dictionary。
#打印每种药物的名称和库存数量。
#如果库存数量小于 10，打印 "Low stock!"。
#计算所有药物的库存总量。
#计算有多少种药物的库存低于 10。

inventory = {"Paracetamol": 50,"Ibuprofen": 15,"Amoxicillin": 8,"Metformin": 30,"Omeprazole": 5}
num_of_low_stuck=0
for drug_name,number in inventory.items():
    if number<10:
        num_of_low_stuck+=1
        print(drug_name,":",number,"-low stock!")
    else:
        print(drug_name,":",number)
print("Total stock:",sum(inventory.values()),"\nLow stock drugs:",num_of_low_stuck)



# %%
#遍历 dictionary，检查每种药物的库存。
#如果库存低于 20，计算需要补充多少件。
#将对应药物的库存更新为 30。
#打印每种需要补货的药物及其补货数量。
#最后打印更新后的 dictionary。

inventory = {"Paracetamol": 50,"Ibuprofen": 15,"Amoxicillin": 8,"Metformin": 30,"Omeprazole": 5}
ideal_stock_num=30
for drug,number in inventory.items():
    if number<20:
        print(drug,":Restock ",ideal_stock_num-number," units")
        inventory[drug]=ideal_stock_num
print("Updated dictionary:\n",inventory)
# %%
#计算每位患者的平均血糖。
#打印患者编号和平均血糖值。
#如果平均血糖大于 7.0，输出 "High glucose"。
#统计平均血糖大于 7.0 的患者数量。
#找出平均血糖最高的患者，并打印其编号和平均值。

glucose = {"P001": [5.2, 5.8, 6.1],"P002": [7.2, 8.1, 7.8],"P003": [4.8, 5.1, 5.3],"P004": [6.5, 7.0, 7.2],"P005": [5.5, 5.9, 6.0]}
num_of_high_glu=0
avers={}
for patient,values in glucose.items():
    aver=sum(values)/len(values)
    avers[patient]=aver
    if aver>7.0:
        print(f"{patient}: {aver:.2f}-high glucose")
        num_of_high_glu+=1
    else:
        print(f"{patient}: {aver:.2f}")
print("Number of high glucose patients:",num_of_high_glu,"\nPatient with highest average:",f"{max(avers,key=avers.get)}({max(avers.values()):.2f})")
# %%
#找第二大的数（corner case）
list=[78,365,65,45,25,74,14,42,47,3,5]
b=list[0]
c=list[1]
if b<c:
    c=b
for a in list:
    if a>b:
        b=a
    elif a>c:
        c=a
print(c)
print(b)
    
        














