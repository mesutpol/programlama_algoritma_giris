#Kodu geliştiren Oğuzhan Demirbaş
#Geliştirilme tarihi 5.11.2023
#Geliştirilme amacı :6 Dilde aynı algoritmayı çalıştırarak arasıdnaki farkları görmek

Satır_yıldız = int(input("Satır sayısını girin: "))#Kullanıcıdan satır sayısı al
Sutun_yıldız = int(input("Sütun sayısını girin: "))#Kullanıcıdan sütün sayısı al

for i in range(Satır_yıldız):#For döngüsünü kullanarak her hücreye "*" ekler
    for j in range(Sutun_yıldız):
        print("*", end="")#end ile ifadenn sonan ne ekleneceği belirlenir
    print()  #İfadesi ile yeni satıra geçilir