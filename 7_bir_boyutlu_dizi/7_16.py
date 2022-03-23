# sezar şifreleme
m=input("kelime: ") ; sm=""; a=int(input("Anahtar:"))
for i in range(len(m)):
    sm+=chr((ord(m[i])-65+a)%26+65)
print("\nşifreli kelime: %s"%sm)
