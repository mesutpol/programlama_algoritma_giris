# Soru: Klavyeden girilen iki basamaklı pozitif tam sayının, onlar ve birler basamağını ayrıştıran programın algoritmasını hazırlayınız.

# Kullanıcıdan iki basamaklı pozitif bir sayı girmesini isteyelim.
sayi = int(input("İki basamaklı pozitif bir sayı girin: "))

# Girilen sayının onlar ve birler basamağını ayrıştıralım
onlar_basamagi = sayi // 10 # Bu işlem direkt olarak onlar basamağını bulmamızı sağlar "//" ifadesi ise bölme işlemini yapar, yalnız kalan kısmını yazmaz.
birler_basamagi = sayi % 10 # Bu işlem direkt olarak birler basamağını bulmamızı sağlar "%" ifadesi ise bölme işlemini yapar, yalnızca kalan kısmını yazar.

# Sonuçları ekrana yazdıralım.
print("Onlar basamağı:", onlar_basamagi)
print("Birler basamağı:", birler_basamagi)

