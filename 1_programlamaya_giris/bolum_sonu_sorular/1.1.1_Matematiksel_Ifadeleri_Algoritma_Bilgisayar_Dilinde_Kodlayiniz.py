try: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    a = float(input("A sayisi: ")) #Kullanıcıdan a sayısını alıyoruz
    a = (1/2)**(((1+a)/(1+(1/a*a))))+((1)/(a*(a**1/2))) #a sayısını formüle göre hesaplıyoruz
    print("Sonuc (y1): ", a) #Sonucu ekrana yazdırıyoruz
except ValueError: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    print("Geçersiz bir sayı girdiniz.") #Hata mesajı veriyoruz
