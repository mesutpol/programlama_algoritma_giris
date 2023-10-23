# Algoritması:
# 1- Kullanıcıdan pozitif sayı al
# 2- Eğer sayı 2 bölünüyorsa sayı çift yaz
# 3- Eğer sayı 2 bölünmüyorsa sayı tek yaz
# 4- Bitir



#Klavyeden girilen pozitif bir tam sayının tek mi ve çift mi olduğunu tespit eden programın algoritmasını hesaplayınız.

sayi = input('Sayı : ') #Kullanıcıdan sayı iste.
if(int(sayi)%2==0):     
      print("Sayı Çift")  #Girilen sayı çift ise ekrana "Sayı Çift" yaz.
else:
      print("Sayı Tek")  #Girilen sayı tek ise ekrana "SayıTek" yaz.

