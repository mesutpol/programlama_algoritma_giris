# 7. Ünite, 15. Ünite Sonu Sorusu
# Sayısal olarak girilen doğum tarihini kelimelerle yazdıran programın akış diyagramını çizip kodlayınız.
sayisalDogumTarihi = input("Doğum Tarihinizi GÜN/AY/YIL olarak giriniz.\n(Gün ve Ay 2 haneli, Yıl ise 4 haneli olarak girilmelidir.)\n")

gun = sayisalDogumTarihi[0:2]
ay = sayisalDogumTarihi[3:5]
yil = sayisalDogumTarihi[6:10]

gunler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", "On", "On Bir", "On İki", "On Üç", "On Dört", "On Beş", "On Altı", "On Yedi", "On Sekiz", "On Dokuz", "Yirmi", "Yirmi Bir", "Yirmi İki", "Yirmi Üç", "Yirmi Dört", "Yirmi Beş", "Yirmi Altı", "Yirmi Yedi", "Yirmi Sekiz", "Yirmi Dokuz", "Otuz", "Otuz Bir"]
aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

print(
gunler[int(gun)],
aylar[int(ay)],
yil, "Tarihinde doğdunuz."
)
# Himmet Can Umutlu - December 29 - 2023 - Happy New Year