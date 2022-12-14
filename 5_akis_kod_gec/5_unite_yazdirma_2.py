a=99
b=123.456             
c="bursa"             
print("%d"%a)         #Tamsayı yazdırma
print("%d"%b)         #Tamsayı yazdırma 
print("%x"%a)         #16 tabanında yazdırma
print("%10.4o"%a)     #8 tabanında yazzdırma 
print("%0.2f"%b)      #Ondalıklı sayı yazdırma
print("%0.8f"%b)      #Ondalıklı sayı yazdırma
print("%10.4e"%b)     #Ondalıklı sayı yazdırma
print("%10.4g"%b)     #Ondalıklı sayı yazdırma
print(a,b,c)
print("%d\t%f\t%f"%(a,b,a+b))
print("%c\t%s\t%d"%(c[0],c,a/3))
d="%s'nın plaka kodu %d'dır"%(c,16)
print(d)