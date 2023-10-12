#Girilen sayının 50'den büyük, küçük veya eşitliğini gösteren program
import math

try:
    inputValue = float(input("Tam sayıyı giriniz: "))
    flooredValue = int(math.floor(inputValue))
    if flooredValue < 50:
        print("Girilen sayı 50'den küçük.")
    elif flooredValue > 50:
        print("Girilen sayı 50'den büyük.")
    else:
        print("Girilen sayı 50'ye eşit.")

except ValueError:
    print("Geçersiz bir sayı girdiniz.")