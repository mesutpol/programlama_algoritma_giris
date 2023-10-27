#Algoritması:
# 1- Başla
# 2- Kullanıcıdan bir tam sayı iste
# 3- sayı eğer > 0 ise pozitif yaz
# 4- sayı eğer < 0 ise negatif yaz
# 5- sayı eğer = 0 ise sayı sıfırdır yaz



#Klavyeden girilen bir tamsayının pozitif, negatif veya sıfır olduğunu tespit eden programın kodu
sayi = int(input("Sayı giriniz: "))# kullanıcadan sayı girmesini istedik#

if (sayi>0) :  # sayi sıfırdan büyük mü bunu kontrol etiriyoruz#
   print("pozitif sayı")# sayi sıfırdan büyükse ekrana pozitif sayı yazar#
elif (sayi<0):# sayi sıfırdan küçük mü bunu kontrol etiriyoruz#
   print("negatif sayı")# sayi sıfırdan küçükse ekrana sayı negatif yazar#
else: # bunların hiç biri değilse bu komut çalışır#
   print("sayı sıfırdır")# ekrana sayı sıfırdır
