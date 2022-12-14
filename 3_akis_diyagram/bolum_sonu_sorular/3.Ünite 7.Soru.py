
#Kenar uzunluğunu Giriniz#
a = int(input("1.Kenarın uzunluğunu giriniz:"))
b = int(input("2.Kenar uzunluğunu giriniz:"))
c = int(input("3.Kenar uzunuluğunu giriniz:"))

#Eğer a,b ve c birbirine eşit değilse#
if (a != b and a != c and b != c):
    print("Çeşitkenar Üçgen!")
#a b c birbirine eşitse#
elif (a == b == c):
    print("Eşkenar Üçgen!")
#iki kenar birbirine eşitse#
else:
    print("İkizkenar Üçgen")