#Kodu yazan Oğuzhan Demirbaş
#Kodu yazma tarihi 12.11.2023

#Boş bir liste oluşturuyoruz.Bu liste,haneleri toplamı tek olan sayıları içerecek.
Tek_haneli_sayılar_lis = []

#1'den 99'a kadar olan sayıları kontrol ediyoruz.
for Sayı in range(1, 100):
    # Her bir sayının hanelerinin toplamını hesaplıyoruz.
    Toplam = sum(map(int, str(Sayı)))#Oluşan listedeki tüm tamsayıları toplar.Yani,örneğin, "41" için 4 + 1 = 5 toplamını elde ederiz.
    
    # Haneler toplamının tek olup olmadığını kontrol ediyoruz.
    if Toplam % 2 == 1:
        # Eğer haneler toplamı tek ise, sayıyı listeye ekliyoruz.
        Tek_haneli_sayılar_lis.append(Sayı)

# Sonuçları ekrana yazdırıyoruz.
print("1 ile 99 arasındaki haneleri toplamı tek olan sayılar:", Tek_haneli_sayılar_lis)




