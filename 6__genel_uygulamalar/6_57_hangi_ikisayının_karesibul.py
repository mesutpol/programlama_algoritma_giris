s=eval(input("pozitif tamsayı: "))
print("\na - b\n=====")
for a in range(0,s+1):
     for b in range(0,s+1):
         if (a**2+b**2==s):
             print("%d-%d"%(a,b))
