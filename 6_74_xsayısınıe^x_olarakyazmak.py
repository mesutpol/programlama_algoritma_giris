import math
N=int(input("terim sayısını giriniz."))
x=eval(input("hesaplanacak x değerini giriniz: ")) ; T=1; F=1
for i in range (1,N):
    F*=i; T+=x**i/F
print("\nSeri açılımı ile e üzeri x değeri: %0.5f"%T)
print("komumtla e üzeri x değeri: %0.5f"%math.exp(x))
