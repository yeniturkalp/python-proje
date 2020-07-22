# -*- coding: utf-8 -*-

x = "Lütfen cümle giriniz = "

kelimeler =  x.split()
kelimeler.sort() 
print(kelimeler)

for kelime in kelimeler:
    print(kelime)