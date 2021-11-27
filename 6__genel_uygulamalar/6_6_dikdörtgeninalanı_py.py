import math

e = int(input("birinci köşegeni giriniz."))
f = int(input("ikinci köşegeni giriniz."))
aci = int(input("aradaki açıyı giriniz."))
pi = 3.14

print (math.sin(aci))
Alan = e*f*math.sin(aci)/2
Alan = (e*f*math.sin(aci*pi/180)/2)
print(Alan)
