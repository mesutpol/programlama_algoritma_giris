#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 9.12.2023

#Hilbert sayısı:Bir eksiği 4'e tam bölünebilen pozitif tam sayılardır.

N=int(input("Kaç adet 'HİLBERT' sayısı oluşturmak istersiniz :"))
#Boş liste oluşturduk
sayi_lis=[]

for k in range (1,N+1):
#Sorunun istediği formül ile hesaplama yaptırıp değişkene aktardık
    sayi=k*4+1
#append metotu ile sayi_lis listesine sayi değişkeninin içindeki değeri ekledik
    sayi_lis.append(sayi)
#Döngü sonundaki listeyi yazdırdık
print(sayi_lis)





