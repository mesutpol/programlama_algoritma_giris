# Fibonacci Serisi
print("fibonacci serisi \n")
N=int(input("Terim sayısı :"))
T1=1; T2=1
print("\n%d\t%d\t"%(T1,T2),end='')
for i in range(1,N-1):
    T3=T1+T2; print("%d\t"%T3,end=''); T1=T2; T2=T3 
