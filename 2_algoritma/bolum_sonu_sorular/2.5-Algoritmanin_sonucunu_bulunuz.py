#Algoritmamizı Yazalım
# print("""Algoritmamız: 
# 1-Başla
# 2- T = 0
# 3- S = 0
# 4- Eğer S>10 ise Git 8
# 5- T=T+2*S
# 6- S=S+2
# 7- Git 4
# 8- Yaz T
# 9- Dur""")

#Şimdi koda dönüştürelim

#Değişkenleri atayalım:
T = 0
S = 0

#Döngüyü tekrarlamak için while komudunu kullanıyoruz 

while S<=10 : #4.Madde : S 10'dan büyük ise T değişkenin içindekini yazdıracak
    T=T+2*S #5.madde : T Değişkenine 2*S+T ekle
    S=S+2 #6.madde S değişkenine 2 ekle

#eğer S 10'dan küçük ya da eşitse altında yazan komutları hep tekrarlar

print(f"Sonuç: {T}") #8.Madde : T'nin içindekini yazıcak