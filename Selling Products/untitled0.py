# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:59:59 2020

@author: Achyut
"""
arr = list()
n = int(input())
for i in range(n):
    arr.append(int(input()))
m = int(input())
count = dict()

for i in arr:
    if i in count.keys():
        count[i]+=1
    else:
        count[i] = 1

count = {k: v for k, v in sorted(count.items(), key=lambda x:x[1])}
temp = 0
for key, value in count.items():
    if(value<=m):
        m-=value
        temp+=1;
    else:
        break
print(len(count)-temp)

            