value = input("Lütfen bir değer girin: ") #Kullanıcıdan bir değer isteniyor.
try:
    value = float(value) #Kullanıcının girdiği değer float olarak değiştiriliyor.

    if value > 50: #Girilen değer 50'den büyükse ekrana "Girilen değer 50'den büyük." yazdırılıyor.
        print("Girilen değer 50'den büyük.")
    elif value < 50: #Girilen değer 50'den küçükse ekrana "Girilen değer 50'den küçük." yazdırılıyor.
        print("Girilen değer 50'den küçük.")
    else: #Girilen değer 50'ye eşitse ekrana "Girilen değer 50'ye eşit." yazdırılıyor.
        print("Girilen değer 50'ye eşit.")

except: #Girilen değer float değil ise ekrana "Hatalı giriş! Lütfen bir sayı girin." yazdırılıyor.
    raise TypeError('Hatalı giriş! Lütfen bir sayı girin.')

