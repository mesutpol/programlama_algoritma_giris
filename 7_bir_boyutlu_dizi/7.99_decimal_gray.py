# Decimal gray
a=int(input("Sayı: ")); s=bin(a)[2:];
print("\nGray kodu: %c"%s[0],end='')
for i in range(1,len(s)):
    print(int(s[i-1]^int(s[i]),end='')
