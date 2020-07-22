# -*- coding: utf-8 -*-

sayı = int(input(" sayı = "))

faktoriyel = 1

if sayı < 0:
    print("Negatif sayıların faktoriyeli yoktur ")
elif sayı == 0:
    print(" Sonuç = 1 ")

else:
    for i in range(1,sayı + 1):
        faktoriyel = faktoriyel * sayı 
    print(" Sonuç = ",faktoriyel)    
        
    