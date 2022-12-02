# Affine şifreleme
m=input("kelime:").upper(); sm==""
a=int(input("Anahtar (a): ")); b=int(input("Anahtar (b): "))
for i in range(len(m)):
  sm+=chr((a*(ord(m[i])-65)+b)%26+65)
print("\nşifreli kelime: %s"%sm)
  
