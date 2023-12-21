#birim dönüştürme 
a=eval (input("uzunluğu giriniz (m) : "))
print ("\nDönüştürme\n1-mm\n2- cm\n3-dm\n4-km\n")
sec=eval (input("Seçiminizi girin : ")); 
if (sec==1):
    b=1000*a
elif (sec==2):
    b=100*a
elif (sec==3):
    c=10*a
elif(sec==4): 
    b=a/1000
else:
    b=0
print("\nSonuç:  %0.5f" %b)

   