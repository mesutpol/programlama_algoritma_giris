# Klavyeden "ss:dd:ss" formatında girilen saat bilgisini,
# toplam dakika olarak yazdıran programın akış diyagramını çizip kodlayınız.

# Saat, Dakika ve Saniye değişkenlerini tanımla ve 0'a eşitle.
saat = 0
dakika = 0
saniye = 0

# Klavyeden "ss:dd:ss" formatında saat bilgisini al.
saat_bilgisi = input("Saat bilgisini girin (ss:dd:ss): ")

# Saat, Dakika, Saniye'yi ayır.
saat, dakika, saniye = map(int, saat_bilgisi.split(':'))

# Toplam dakikayı hesapla.
toplam_dakika = saat * 60 + dakika

# Toplam dakikayı ekrana yazdır.
print(f"Toplam Dakika: {toplam_dakika}")