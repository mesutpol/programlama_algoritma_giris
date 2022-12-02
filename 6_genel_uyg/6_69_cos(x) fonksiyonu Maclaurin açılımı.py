# cosinüs
import math
aci=eval(input("Açı değeri (derece): "))
N=int(input("Terim sayısı: "))
T=1; x=math.radians(aci)
for i in range(1,N):
  T+=(-1)**i*x**(2*i/math.factorial(2*i)
print("\nSeri açılımı ile hesaplanan değer: %.0.5f"%T)
print("komutla hesaplanan değer: %.05f"%math.cos(x))
