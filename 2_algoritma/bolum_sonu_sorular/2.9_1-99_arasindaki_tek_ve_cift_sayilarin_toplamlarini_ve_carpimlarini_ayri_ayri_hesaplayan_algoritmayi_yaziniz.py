#Tek Sayılar Toplamları
tekSayiİlkDegeri = 3
tekSayiSonDegeri = 97
sonuc = (tekSayiSonDegeri - tekSayiİlkDegeri) / 2 + 1
sonuc = int(sonuc**2)
print("1'den 99'a Kadar Olan Tek Sayıların Toplamı:\n",sonuc)

#Çift Sayılar Toplamları
ciftSayiİlkDegeri = 2
ciftSayiSonDegeri = 98
sonuc = (ciftSayiSonDegeri - ciftSayiİlkDegeri) /2 + 1
sonuc = int(sonuc**2)
print("1'den 99'a Kadar Olan Çift Sayıların Toplamı:\n",sonuc)

#Tek Sayılar Çarpımları
tekCarpim = 1
for tekSayi in range(3, 98, 2):
    tekCarpim *= tekSayi
print("1'den 99'a Kadar Olan Tek Sayıların Çarpımı:\n",tekCarpim)

#Çift Sayılar Çarpımları
ciftCarpim = 1
for ciftSayi in range(2, 99, 2):
    ciftCarpim *= ciftSayi
print("1'den 99'a Kadar Olan Çift Sayıların Çarpımı:\n",ciftCarpim)

