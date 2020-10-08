# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:23:12 2020

@author: Achyut

Statement
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.

Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

Example input
5
3
5
2
1

Example output
4
"""

a = set()
n = int(input())
#a.add(n)
for i in range(1, n):
  a.add(int(input()))

for i in range(1, n+1):
  if i not in a:
    print(i)
    
        



