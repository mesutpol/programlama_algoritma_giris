#Kodu yazan-->Ramazan Polat
#Yazılma tarihi-->10.12.2023

mo=float(input("Başlangıç kütlesini gram cinsinden giriniz mo:"))
dt=float(input("Yarılanma süresini saniye cinsinden giriniz dt:"))
t=float(input("Saniye cinsinden süreyi giriniz t:"))
n=t/dt
km=mo/(2**n)
print(n,"Yarılanma geçirmiştir")
print(int(km),"gr kütlesi kalmıştır")