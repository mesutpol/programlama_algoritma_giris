#Kodu yazan-->Ramazan Polat
#Yazılma tarihi-->10.12.2023
#Klavyeden başlangıç kütlesi ile yarılanma süresi girilen bir radyoaktif elementin belirtilen süre sonunda kaç yarılanma geçireceğini ve kütlesinin ne kadar kalacağını hesaplayan program 

mo=float(input("Başlangıç kütlesini gram cinsinden giriniz mo:"))
dt=float(input("Yarılanma süresini saniye cinsinden giriniz dt:"))
t=float(input("Saniye cinsinden süreyi giriniz t:"))
n=t/dt
km=mo/(2**n)
print(n,"Yarılanma geçirmiştir")
print(int(km),"gr kütlesi kalmıştır")
