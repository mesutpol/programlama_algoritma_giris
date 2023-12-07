try: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    a = float(input("A sayisi: ")) #Kullanıcıdan a sayısını alıyoruz
    b = float(input("B sayisi: ")) #Kullanıcıdan b sayısını alıyoruz
    y3 =(3**((a+b)/((a*a+b*b) **4)) / (a*b/(1+(1/(a+(1/(b+((a*b)**2)**1/5)))))))+((a**2+b**3)/((a*b)/a**2+b**2+2*a*b)+3*(a**2)-3*(b**2))- ((1/4)**(a**3))/(2/((b**2)**(1/3))) # Formülü Uyguluyoruz
    print("Sonuc (y3): ", y3) #Sonucu ekrana yazdırıyoruz
except ValueError: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    print("Geçersiz bir sayı girdiniz.") #Hata mesajı veriyoruz
