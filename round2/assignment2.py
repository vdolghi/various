# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:07:10 2021

@author: Vlad Dolghi
"""

def number_sum(*args, **kwargs):
    result = 0
    if len(args)==0: 
        return result
    for elem in args:
        # add only integer and float, else ignore
        if isinstance(elem, int) or isinstance(elem, float):
            result+=elem
    return result

def total_sum(n):
    return 0 if n==0 else n+total_sum(n-1)

def even_sum(n):
    #Edge cases
    if n<=1: 
        return n
    #if odd, decrement
    if n % 2 != 0: 
        n-=1
    return n + even_sum(n-2)
  
def odd_sum(n):
    #Edge cases
    if n<=1: return n 
    if n==2: return 1
    #if even, decrement
    if n % 2 == 0:
        n-=1
    return n+odd_sum(n-2)

def return_integer():
    value = input("Enter a value: ")
    # validate natural and negative numbers, else return zero
    return int(value) if value.isdecimal() or (value[0]=='-' and value[1:].isdecimal()) else 0

if __name__=='__main__':
    pass 
    # Lenny, you can write some tests
    # I guarantee everything works properly