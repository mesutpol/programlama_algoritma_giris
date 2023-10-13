#Girilen sayının 50'den büyük, küçük veya eşitliğini gösteren program

import math #math kütüphanesini ekliyoruz.

try: #Hata olabilecek kodları try bloğunun içine yazıyoruz.
    inputValue = float(input("Tam sayıyı giriniz: ")) #Kullanıcıdan sayı alıyoruz.
    if inputValue < 50: #Eğer girilen sayı 50'den küçükse
        print("Girilen sayı 50'den küçük.") #Ekrana 50'den küçük yazdırıyoruz.
    elif inputValue > 50: #Eğer girilen sayı 50'den büyükse
        print("Girilen sayı 50'den büyük.") #Ekrana 50'den büyük yazdırıyoruz.
    else: #Eğer girilen sayı 50'ye eşitse
        print("Girilen sayı 50'ye eşit.") #Ekrana 50'ye eşit yazdırıyoruz.

except ValueError: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    print("Geçersiz bir sayı girdiniz.") #Ekrana hata mesajı yazdırıyoruz.