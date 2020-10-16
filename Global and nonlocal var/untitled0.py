# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:04:58 2020

@author: Achyut
"""

def funct_1():
    global a 
    a = 10
    print(a)

funct_1()

def funct_2():
    print(a)

funct_2()

def funct_3():
    x = 40
    def func_4():
        #nonlocal x
        x = 2
        print(x)
    func_4()
    print(x)

funct_3()




