



# Başla 
# ilk sayı giriniz(f)
# ikinci sayı giriniz(s)
# üçüncü sayı giriniz(t)
# Eğer (f,s,t)sayı değiilse git 12
# f,s,t değişkenlerini tam sayıya çevir
# f,s,t değişkenlerini diziye aktar (liste)
# liste dizisinin elemanlarını küçükten büyüğe sırala
# yazdır (liste)
# dur
# yazdır (lütfen sayı giriniz)
# dur





f=input("İlk sayi ?  ")
s=input("İkinci sayi ?  ")
t= input("üçüncü sayi ?  ")

if (f.isnumeric() and s.isnumeric() and t.isnumeric()):
    f=int(f)
    s=int(s)
    t=int(t)
    liste=[f]+[s]+[t]
    liste.sort()
    print(liste)
else:
    print("Lütfen sayi giriniz!")   
    