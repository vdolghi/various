# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:57:03 2021

@author: Vlad Dolghi
"""
import math
import webbrowser

class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        if numitor != 0:
            self.numitor = numitor
        else:
            raise ZeroDivisionError("Cannot divide by zero!")
        
    def __str__(self):
        return str(self.numarator) + "/"+ str(self.numitor)
    
    def __sub__(self, other):
        if not isinstance(other, Fractie):
            raise TypeError("Fraction argument expected!")
        m = self.numitor * other.numitor
        n = self.numarator * other.numitor - self.numitor*other.numarator
        gcd = math.gcd(n,m)
        if gcd > 1: 
            n, m = n // gcd, m // gcd
        return Fractie(n,m)
    
    def __add__(self, other):
        if not isinstance(other, Fractie):
            raise TypeError("Fraction argument expected!")
        m = self.numitor * other.numitor
        n = self.numitor * other.numarator + self.numarator*other.numitor
        gcd = math.gcd(n,m)
        if gcd > 1: 
            n, m = n // gcd, m // gcd
        return Fractie(n,m)
    
    def __mul__(self, other):
        if not isinstance(other, Fractie):
            raise TypeError("Fraction argument expected!")
        m = self.numitor * other.numitor
        n = self.numarator * other.numarator
        gcd = math.gcd(n,m)
        if gcd > 1: 
            n, m = n // gcd, m // gcd
        return Fractie(n,m)
    
    def __truediv__(self, other):
        if not isinstance(other, Fractie):
            raise TypeError("Fraction argument expected!")
        m = self.numitor * other.numarator
        n = self.numarator * other.numitor
        gcd = math.gcd(n,m)
        if gcd > 1: 
            n, m = n // gcd, m // gcd
        return Fractie(n,m)
    
    def inverse(self):
        return Fractie(self.numitor,self.numarator)
    
if __name__=='__main__':
    print('*'*20 +'\nFRACTII PENTRU LENNY\n' + '*'*20)
    f = Fractie(5, 6)
    print(f'f = {f}')
    g = Fractie(3, 4)
    print(f'g = {g}')
    print(f'f + g = {f+g}')
    print(f'f - g = {f-g}')
    print(f'f * g = {f*g}')
    print(f'f / g = {f/g}')
    print(f'Inverse of f = {f.inverse()}')
    input("Press any key to continue...")
    webbrowser.open_new('https://www.youtube.com/watch?v=FLAvp6HtXf0')