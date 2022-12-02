#kombinasyon
f1=f2=f3=1; n=int(input("n: ")) ; r=int(input("r: "))
for i in range (1,n+1):
    f1*=i
    if (i<=r):
        f2*=i
    if (i<=n-r) :
        f3*=i
        
k=f1/(f2*f3)
print("\nSonuç=%d"%k)     
