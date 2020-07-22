# -*- coding: utf-8 -*-

def topla(sayı1,sayı2):
    return sayı1 + sayı2

def çıkar(sayı1,sayı2):
    return sayı1 - sayı2

def çarp(sayı1,sayı2):
    return sayı1 * sayı2

def böl(sayı1,sayı2):
    return sayı1 / sayı2

print("OPERASYON: ")
print("1: topla ")
print("2: çıkar ")
print("3: çarp")
print("4: böl")

seçim = input("SEÇİMİNİZ ? ")

sayı1 = int(input("BİRİNCİ SAYI = "))
sayı2 = int(input("İKİNCİ SAYI = "))

if seçim =='1':
    print("topla = " + str(topla(sayı1,sayı2)))
    
elif seçim =='2':
    print("çıkar = " + str(çıkar(sayı1,sayı2)))   
    
elif seçim =='3':
    print("çarp = " + str(çarp(sayı1,sayı2)))


elif seçim =='4':
    print("böl = " + str(böl(sayı1,sayı2)))        
else:
    print("GEÇERSİZ SEÇİM ")
    
    
    
    