# Ornek 8.4
# Klavyeden girilen NxN tipindeki A ve B kare matrislerini toplayan (C = A + B) program.

# ------------------------------------------------------------------------------
# numpy kutuphanesini kullanmadan yapilmak istenirse:
# ------------------------------------------------------------------------------
# her girilecek matrisin ayni boyutlarda olacagindan sadece bir kere
# sorulmasi yeterlidir.
N=int(input("Kare matrisin tipini giriniz: "))

# kare matrikslerini olustur.
A=[[[] for i in range(N)] for j in range(N)] # birinci kare matriksini olustur
B=[[[] for i in range(N)] for j in range(N)] # ikinci kare matriksini olustur
C=[[[] for i in range(N)] for j in range(N)] # A ve B toplamiyla elde edilecek
                                             # kare matriksini olustur.

# Kullanicidan matriks eleman degerlerini al
# birinci matriks icin
for i in range(N):
    for j in range(N):
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))
# ikinci matriks icin
for i in range(N):
    for j in range(N):
        B[i][j]=int(input("B(%d,%d= "%(i+1,j+1)))

# hepsini karsilik gelen yerlerde topla ve C matriksine koy.
for i in range(N):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]

# yazdir elemanlari
print(C)

# ------------------------------------------------------------------------------
# numpy kutuphanesini kullanarak(kitaptaki tekli python ornegi):
# ------------------------------------------------------------------------------
#matris toplami
import numpy as np # numpy ile ilgili aciklama ornek 8_1 de mevcut
print("Matrisleri [a b;c d] seklinde giriniz\n")

print("\nA matrisi\n---------")
x=input()
A=np.matrix(x)

print("\nB matrisi\n---------")
x=input()
A=np.matrix(x)

C=A+B

print("\nC=A+B matrisi\n-------")
print(C)
