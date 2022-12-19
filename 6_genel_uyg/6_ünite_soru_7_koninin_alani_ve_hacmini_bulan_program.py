#koninin yüzey alanı ve hacmini hesaplayan algoritma#
import math
p = math.pi
r = float(input("yarıçapı giriniz: "))
h = float(input("yüksekliği giriniz: "))

alan = (math.sqrt(r*r+h*h)+r)*(r*p)

hacim =(1/3)*p*(r*r)*h

print("koninin alanı: ",alan)
print("koninin hacmi: ",hacim)