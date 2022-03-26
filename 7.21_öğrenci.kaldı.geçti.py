import math
A=[]
toplam=0
ort=0

N=input(print("kaç not gireceğinizi yazınız"))
N=int(N)

for i in range(N):
    print("%d. notları giriniz"%i)
    A.append(int(input(i)))
    toplam=toplam+A[i]

ort=toplam/N

for i in range(N):
    if A[i]<ort:
        print("%d nolu öğrenci kaldı"%(i+1))
    elif A[i]>ort:
        print("%d nolu öğrenci geçti"%(i+1))

            