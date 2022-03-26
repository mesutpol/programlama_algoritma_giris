A=[]
N=int(input("Dizinin eleman sayısını giriniz:"))
for i in range(N):
    print("A(%d)="%(i+1),end='')
    A.append(int(input()))
for i in range(N-1):
    for j in range(i+1,N):
        if(A[j]<A[i]):
            g=A[i]
            A[i]=A[j]
            A[j]=g
print("\nSıralı dizi\n=======")
for i in range(N):
    print("A(%d)=%d"%(i+1,A[i]))
