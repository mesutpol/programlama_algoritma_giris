# Toplamlar
n=int(input("pozitif tamsayı giriniz: "))
t1=t2=t3=0
for i in range(1,n+1) :
    t1+=i
# Döngü yerine t1=suum(range(1,n+1,1))
for i in range(1,n+1,2) :
    t2+=i
# Döngü yerine t2=sum(range(1,n+1,2))
for i in range(2,n+1,2) :
    t3+=i
# Döngü yerine t3=sum(range(2,n+1,2))
print("\n1'den %d'ye kadar sayıların toplamı:"%n,t1)
print("1'den %d'ye kadar tek sayıların toplamı:"%n,t2)
print("2'den %d'ye kadar sayıların toplamı:"%n,t3)
