# Polinom değeri hesaplama
import numpy as np
a=[]; n=int(input("y(x) polinomunun derecesi: "))
for i in range(n+1):
  print("x^%d nin katsayısı: "%i,end=''); a.append(eval(input()))
a.reverse(); b=eval(input("Hesaplanacak x değeri: "))
print("\ny(%0.3f)=%0.5f"%(b,np.polyvall(a,b)))
