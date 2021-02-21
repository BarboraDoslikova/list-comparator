# -*- coding: utf-8 -*-
"""
Generate two lists (of different sizes) of integers
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates) sorted from highest to lowest.

@author: Barbora Doslikova
"""
import numpy as np

listA = np.random.randint(1,10,15)
listB = np.random.randint(1,20,10)

listJoint = []

for i in listA:
    if i in listB:
        if i not in listJoint:
            listJoint.append(i)

listJoint.sort()
listJoint.reverse()

print(listA, listB, listJoint)