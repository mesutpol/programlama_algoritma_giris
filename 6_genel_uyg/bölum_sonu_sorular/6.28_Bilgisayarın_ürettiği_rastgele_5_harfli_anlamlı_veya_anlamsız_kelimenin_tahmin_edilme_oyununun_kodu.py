#Bilgisayarın ürettiği rastgele 5 harfli anlamlı veya anlamsız kelimenin tahmin edilme oyunun kodu.


import random  
##Random modülü rastgele işlem oluşturmak için kullanılır.

def rastgele_kelime():
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    harfler = random.sample(alfabe, 5)
    return "".join(harfler)
#26 harften rastgele 5 tane seçip birleştirme işlemi yapar.

def tahmin_oyunu():
    kelime = rastgele_kelime()
    hak = 5 #Tahmin hakkı değeri atanır.
    tahminler = []

    while hak > 0:    #Tahmin hakları döngüye girer, input olan tahmin eğer rastgele kelime ile eşleşemezse döngü tekrarlanır (hak dolana kadar)
        print("**Tahmininiz: **")
        tahmin = input()
        tahminler.append(tahmin)

        if tahmin == kelime:
            print("**Kelime Doğru.**")
            break

        if tahmin not in kelime:
            hak -= 1
            print(f"**Kelime Yanlış. Kalan haklarınız: {hak}**")

        if hak == 0:
            print(f"**Hakkınız Doldu. Doğru kelime: {kelime}**")  # Tahmin hakkı dolunca eğer kelime doğru tahmin edilmemişse ekrana doğru kelime yazılır.

tahmin_oyunu()
