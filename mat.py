# -*- coding: utf-8 -*-


static void Main(string[] args)
        {
            int sayi, yuzler, onlar, birler;
            Console.Write("Sayıyı Girin : ");
            sayi = Convert.ToInt32(Console.ReadLine());
            yuzler = sayi / 100;
            sayi = sayi - (yuzler * 100);
            onlar = sayi / 10;
            sayi = sayi - (onlar * 10);
            birler = sayi;
            Console.WriteLine("Yüzler Basamağı : " + yuzler);
            Console.WriteLine("Onlar Basamağı : " + onlar);
            Console.WriteLine("Birler Basamağı : " + birler);
            Console.ReadKey();
        } 
        
        
x = sayı 
y = yüzler
z = onlar
c = birler

int(input("lütfen sayı giriniz"))

