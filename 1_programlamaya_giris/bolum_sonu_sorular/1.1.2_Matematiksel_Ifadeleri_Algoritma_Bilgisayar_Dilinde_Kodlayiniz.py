try: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    a = float(input("A sayisi: ")) #Kullanıcıdan a sayısını alıyoruz
    b = float(input("B sayisi: ")) #Kullanıcıdan b sayısını alıyoruz
    y2 = (a+(a/(b+1)/((1+(((a+b*b)**1/3))/(1/((a*b)**(1/2))**(1/5))))+((a*b)**2)-4/(a/((b*b)**1/3))))
    print("Sonuc (y2): ", y2) #Sonucu ekrana yazdırıyoruz
except ValueError: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    print("Geçersiz bir sayı girdiniz.") #Hata mesajı veriyoruz
