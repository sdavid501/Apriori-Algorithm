#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from itertools import combinations

print("==================Welcome to Apriori Algorithm Module====================", "\n\n")
print("Select database: ")
print("For Amazon, press 1")
print("For Nike, press 2")
print("For K-Mart press 3")
print("For Best Buy, press 4")
print("For Generic Data, press 5")
print("For Custom Data, press 6")
print("For Homework 1 Data, press 7")

while True:
    try:
        selectedDatabase = int(input())
    except:
        print("Please select a valid number")
        continue
    if selectedDatabase == 1:
        print("You've selected Amazon database")
        data = pd.read_csv("Amazon.csv")
        transaction = pd.read_csv("AmazonTransactions.csv")
        break
    elif selectedDatabase == 2:
        print("You've selected Nike database")
        data = pd.read_csv("Nike.csv")
        transaction = pd.read_csv("NikeTransactions.csv")
        break
    elif selectedDatabase == 3:
        print("You've selected K-Mart database")
        data = pd.read_csv("K-mart.csv")
        transaction = pd.read_csv("KMartTransactions.csv")
        break
    elif selectedDatabase == 4:
        print("You've selected Best Buy database")
        data = pd.read_csv("BestBuy.csv")
        transaction = pd.read_csv("BestBuyTransactions.csv")
        break
    elif selectedDatabase == 5:
        print("You've selected Generic database")
        data = pd.read_csv("Generic.csv")
        transaction = pd.read_csv("GenericTransactions.csv")
        break
    elif selectedDatabase == 6:
        print("You've selected Custom database")
        data = pd.read_csv("CustomData.csv")
        transaction = pd.read_csv("CustomDataTransactions.csv")
        break
    elif selectedDatabase == 7:
        print("You've selected Homework 1 database")
        data = pd.read_csv("Hw1.csv")
        transaction = pd.read_csv("Hw1Transactions.csv")
        break
    else:
        print("Please select a valid number from the options above")

ms = "N"
while not(ms == "Y" or ms == "y"):
    print("Set minimum support (%):")
    try:
        minSupport = float(input())
    except:
        print("Please enter a valid number")
        continue
    print("You've set the minimum support as ", minSupport, "%")
    if(minSupport > 100): 
        print("The minimum support can't be greater than 100%")
        continue
    print("press Y to continue otherwise any other character to change the minimum support")
    ms = input()

ms = "N"
while not(ms == "Y" or ms == "y"):
    print("Set confidence (%):")
    try:
        confidence = float(input())
    except:
        print("Please enter a valid number")
        continue
    print("You've set the confidence as ", confidence, "%")
    if(confidence > 100): 
        print("The confidence can't be greater than 100%")
        continue
    print("press Y to continue otherwise any other character to change the confidence")
    ms = input()
minSupportValue = int(np.ceil(minSupport/100 * len(transaction)))

dataDict = {}
transactions = []
itemsets = []

for i in data[data.columns[-1]]:
    itemsets.append(i.upper())

for trans in transaction[transaction.columns[-1]]:
    trans = trans.split(',')
    trans = [i.upper().strip() for i in trans]
    transactions.append(trans)

print(itemsets)
transactions


# In[2]:



status = True
combCount = 1
dataDict = {}
while status and combCount <= len(transactions):
    combData = combinations(itemsets, combCount)
    temp ={}
    for com in combData:
        for trans in transactions:
            count = 0
            for i in com:
                count += trans.count(i)
            if count == len(com):
                strs = ",".join(com)
                if strs in temp:
                    temp[strs] += 1
                else:
                    temp[strs] = 1
    for i in temp:
        if i in dataDict:
            dataDict[i] += temp[i]
        else:
            dataDict[i] = temp[i]
    combCount += 1
print("============================ FREQUENT ITEMSETS ============================")
assoItems = {}
for i in dataDict:
    if dataDict[i] >= minSupportValue:
        assoItems[i] = dataDict[i]
        print(i)

print("========= ALL ASSOCIATION RULES (Min Support: " 
      +str(minSupport)+" Confidence:" +str(confidence)+")=========")

for i in assoItems:
    if len(i.split(',')) < 2:
        continue
    assoList = i.split(',')
    nItem = assoItems[i]
    altWords = []
    for j in range(1,len(assoList)):
        comb = combinations(assoList, j)
        combWords = [w for w in comb]
        d = len(combWords) - 1
        for c in range(len(combWords)):
            altWords.append(combWords[c])

    n = len(altWords) - 1
    for w in range(len(altWords)):
        item1 = ",".join(altWords[w])
        item2 = ",".join(altWords[n-w])
        
        nTransactions = len(transactions)
        support = (nItem/nTransactions)* 100
        
        if item1 in assoItems and support >= minSupport:
            nItem1 = assoItems[item1]
            conf1 = (nItem/nItem1)* 100
            if conf1 >= confidence:
                print(item1, '->', item2, " | Support = " + str(support)+'%', 
                 " | Confidence = " + str(conf1)+'%')
        
        


# In[ ]:




