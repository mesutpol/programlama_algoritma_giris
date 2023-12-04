# Uzunluk birimleri arasında dönüşüm yapan program

def uzunluk_donustur(mevcut_uzunluk, mevcut_birim, hedef_birim):
    # Mevcut uzunluk değerini ve dönüştürülecek birimi değişkenlere ata
    if mevcut_birim == "km":
        mevcut_uzunluk = mevcut_uzunluk * 1000
    elif mevcut_birim == "hm":
        mevcut_uzunluk = mevcut_uzunluk * 100
    elif mevcut_birim == "dam":
        mevcut_uzunluk = mevcut_uzunluk * 10
    elif mevcut_birim == "dm":
        mevcut_uzunluk = mevcut_uzunluk * 0.1
    elif mevcut_birim == "cm":
        mevcut_uzunluk = mevcut_uzunluk * 0.01
    elif mevcut_birim == "mm":
        mevcut_uzunluk = mevcut_uzunluk * 0.001
    elif mevcut_birim == "m":
        mevcut_uzunluk = mevcut_uzunluk

    # Hedef birimi belirle
    if hedef_birim == "km":
        hedef_uzunluk = mevcut_uzunluk / 1000
    elif hedef_birim == "hm":
        hedef_uzunluk = mevcut_uzunluk / 100
    elif hedef_birim == "dam":
        hedef_uzunluk = mevcut_uzunluk / 10
    elif hedef_birim == "dm":
        hedef_uzunluk = mevcut_uzunluk * 10
    elif hedef_birim == "cm":
        hedef_uzunluk = mevcut_uzunluk * 100
    elif hedef_birim == "mm":
        hedef_uzunluk = mevcut_uzunluk * 1000

    # Dönüştürülmüş değeri ekrana yazdır
    print(f"{mevcut_uzunluk} {mevcut_birim} = {hedef_uzunluk} {hedef_birim}")


# Kullanıcıdan girişleri al
mevcut_uzunluk = float(input("Mevcut uzunluk değerini giriniz (km, hm, dam, dm, cm, mm): "))
mevcut_birim = input("Mevcut uzunluk birimini giriniz: ")
hedef_birim = input("Hedef uzunluk birimini giriniz: ")

# Dönüşüm işlemini gerçekleştir
uzunluk_donustur(mevcut_uzunluk, mevcut_birim, hedef_birim)
