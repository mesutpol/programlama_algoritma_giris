#6. Ünite Bölüm Sonu Soruları, 7. Soru: Klavyeden girilen yarıçap ve yükseklik değerine göre koninin yüzey alanı ve hacmini hesaplayan programın akış diyagramını çizip kodlayınız.
import math

pi = float(input("Pi sayısının baz alınacağı değeri girin:\n"))
r = float(input("Yarıçap değeri girin:\n"))
h = float(input("Yükseklik değeri girin:\n"))
l_Kare = float(h**2 + r**2)
l = float(math.sqrt(l_Kare))
hacim = float(1/3 * pi * r**2 * h)
yuzeyAlani = float(pi * r**2 + pi * r * l)

print("Hacim:\n", hacim)
print("Yüzey Alanı:\n", yuzeyAlani)
#Himmet Can Umutlu - November 03 - 2023