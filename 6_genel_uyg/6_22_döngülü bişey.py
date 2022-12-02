n=int(input("pozitif tamsayı giriniz="))
t1=0
t2=0
t3=0
for i in range(1,n+1):
    t1+=i
t1=sum(range(1,n+1,1))    

for i in range(1,n+1,2):
    t2+=i
t2=sum(range(1,n+1,2))

for i in range(2,n+1,2):
    t3+=i
t3=sum(range(2,n+1,2))
print("",t1)
print("",t2)
print("",t3)
