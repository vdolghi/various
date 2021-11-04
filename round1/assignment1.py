# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 21:38:09 2021

@author: Vlad Dolghi
"""

from pprint import pprint

print ("Liste pentru Lenny, multe-multe...\n")
l1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
l2 = list(sorted(l1))
l3 = list(sorted(l1, reverse=True))
l4 = l2[1::2]
l5 = l2[::2] 
l6 = l2[2::3]

pprint(l1)
pprint(l2)
pprint(l3)
pprint(l4)
pprint(l5)
pprint(l6)