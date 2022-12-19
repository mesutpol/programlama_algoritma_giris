Soru = klavyeden üç kenarı girilen bir üçgenin türünü (eşkenar,ikizkenar veya çeşitkenar) olduğunu tespit eden programın akış diyagramını çizip yazılımını yazınız.

Cevap = 

yazılımı=
a = int(input("1.bir kenar giriniz:")) 
b = int(input("2.kenarı giriniz:")) 
c = int(input("3.kenarı giriniz:"))

if (a==b and b==c and a==c) :
    print("eşit kenar") #girilen değerde a=b=c ise eşit kenar üçgen olur.
elif (a==b and b!=c and a!=c):
    print("ikizkenar üçgen")  #girilen değerde a ve b eşit c onlardan farklı ise ise ikiz kenar kenar üçgen olur
else:
    print("çeşitkenar üçgen") #girilen tüm değerler farklı olsursa çeşitkenar üçgen olur.
    

Akış Diyagramı = 
!(soru2)[6.ünite 2.soru.png]
