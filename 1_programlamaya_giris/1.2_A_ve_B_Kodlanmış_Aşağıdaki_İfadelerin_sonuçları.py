#Soruda verilen sayılar
A = 25 
B = 36 

x = int(input("Kaçıncı ifade (1'den 8 e kadar bir sayı): "))

if x != round(1,9):      #Eğer farklı bir girerse vereceği hata
    print("Lütfen 1 ile 8 arası sayı giriniz.")

#İşlemleri çalışmasına sağlıyan kodlar

if x == 1:
    print(A**1/2+B**1/2) #1.İfade burdaki 1/2 parantez olmadıgından dolayı kök olarak alanmaz sayının yarısını alır

if x == 2:
    print(A**(1/2)+B**1/2) #2.İfade (1/2) parantez için olması kök anlamına geliyor

if x == 3:
    print(A**1/2+B**(1/2)) #3.İfade

if x == 4:
    print(A**(1/2)+B**(1/2)) #4.İfade

if x == 5:
    print((A**1/2+B)**1/2) #5.İfade

if x == 6:
    print((A**(1/2)+B)**1/2) #6.İfade

if x == 7:
    print((A**(1/2)+B)**(1/2)) #7.İfade

if x == 8:
    print((A+B)**(1/2)) #8.İfade

# A üstü 1/2 alırken A**(1/2) Kullanırız.
