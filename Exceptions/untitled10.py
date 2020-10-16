# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:49:07 2020

@author: Achyut
"""
try:
    print(11/0)
except Exception as e:
    print(e)

a = 5
if a>2:
    raise Exception("a greater than 2!")