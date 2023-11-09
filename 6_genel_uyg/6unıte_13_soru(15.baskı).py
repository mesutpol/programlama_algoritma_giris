# Kullanıcıdan ondalıklı sayıyı alın
sayi = float(input("Bir ondalıklı sayı girin: "))

# Sayının tam kısmını ve ondalık kısmını ayırın
tam_kisim = int(sayi)
ondalik_kisim = sayi - tam_kisim

# Sonuçları ekrana yazdırın
print("Tam Kısım:", tam_kisim)
print("Ondalık Kısım:", ondalik_kisim)


'''
Başla
1. Kullanıcıdan bir ondalıklı sayı girmesini iste ve bu değeri "sayi" değişkenine kaydet.
2. "sayi" değişkenini tam kısmı ve ondalık kısmı olarak ayırın. Tam kısmı "tam_kisim" değişkenine, ondalık kısmı ise "ondalik_kisim" değişkenine kaydedin.
3. "tam_kisim" ve "ondalik_kisim" değerlerini ekrana yazdır.
4. Programı sonlandır.

'''