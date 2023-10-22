# Kullanıcıdan aldığımız iki basamaklı sayıyı onlar ve birler basamağını ekrana yazdıran algoritma ve program :


# ALGORİMA



# Başla
# f oku 
# Eğer 10 <= f <= 99
# o=f // 10 (f i 10 a böl tamsayıyı o ya aktar )
# b=f % 10 (f i 10 a böl kalanı b ye aktar )
# Yazdır o
# Yazdır b
# Dur
# Yazdır (Geçersiz sayı !!!)
# Dur


#PROGRAMI


f = int(input("Lütfen iki basamaklı bir pozitif tam sayı girin: "))

if 10 <= f <= 99:
  
    o= f // 10
    b = f % 10

    print(f"Sayının onlar basamağı: {o}")
    print(f"Sayının birler basamağı: {b}")
else:
    print("Geçersiz giriş!")
