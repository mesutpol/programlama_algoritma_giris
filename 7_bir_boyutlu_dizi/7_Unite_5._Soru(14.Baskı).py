#Kodu yazan Oğuzhan Demirbaş
#Kodun yazım tarihi 15.12.2023

A=[] # Boş bir  A listesi oluşturduk.
B=[] # Boş bir  B listesi oluşturduk.
C=[] # Boş bir  C listesi oluşturduk.

n=int(input("Bir 'n' değeri giriniz :")) # Kullanıcıdan 'n' değeri alınıyor.

for i in range(0,n): # Her bir A ve B listesinin elemanları için kullanıcıdan giriş alınıyor ve listelere ekleniyor
    A.append(int(input("A(%d)="%(i+1))))
    B.append(int(input("B(%d)="%(i+1))))

for m in range(0,n):
    toplam=A[m]+B[m] # A ve B listelerindeki indekslere karşılık gelen elemanların toplamını hesapla
    C.append(toplam) # sonuçları C listesine ekle.

    print(8 * "*") # Görsel açıdan konuldu çıktının okunaklı olmaı için
    print("C(%d)=%d"%(m+1,toplam)) # Bulunan toplam sonucu ve indeksi ekrana yazdırdık
print(8 * "*") # Görsel açıdan konuldu çıktının okunaklı olmaı için
