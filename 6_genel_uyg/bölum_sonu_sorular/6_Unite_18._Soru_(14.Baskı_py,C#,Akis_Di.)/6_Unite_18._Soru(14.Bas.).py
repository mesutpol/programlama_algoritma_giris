#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 14.12.2023

Sayi=int(input("Sayıyı giriniz :"))#Sayi değeri kullanıcıdan alındı

Sayi_str=str(Sayi)#Sayi_str değişkenine sayi değerini str cinsinde atıyoruz

liste=[]#Boş bir liste belirledik
for i in range(0,len(Sayi_str)):#Döngü açtık ve len ile karakter uz.kullanarak son belirledik
     liste.append(int(Sayi_str[i]))#listeye append ile sayi_str değişkenini intager formatında ekledik
     i+=1#i yi 1 arttırdık
print(sum(liste))#sum ile listedeki elemanları topladık ve print ile yazdırdık

