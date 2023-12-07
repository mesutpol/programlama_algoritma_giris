#10-99 arasındaki "bağdaşık sayılar"ın listesini veren programın kodu

# Sayıları tutmak için boş bir liste oluştur
bagdasi_sayilar = []

# 10 ile 99 arasındaki tüm sayıları teker teker incele
for sayi in range(10, 100):
    # Her sayı için bölümleme yap ve elde edilen kalanları sakla
    bölümleme_kalanlari = [sayi % i for i in range(2, int(sayi**0.5) + 1)]
    
    # Bağdaşık sayılar için bir kontrol yap
    if len(set(bölümleme_kalanlari)) == 1:
        bagdasi_sayilar.append(sayi)

print(bagdasi_sayilar)