# Ornek 8.5
# Klavyeden girilen NxN tipindeki A matrisinin izini (ana kosegen uzerindeki
# elemanlarin toplamini) hesaplayip yazdiran program.

# ------------------------------------------------------------------------------
# numpy kutuphanesini kullanmadan yapilmak istenirse:
# ------------------------------------------------------------------------------

# matrisin izini bulma fonksiyonu
# matrisin bulundugu degisken "mat", matrisin tipi "N"
# Void kullanildi return type icin cunku geriye getirmesine gerek yok
# bulunan degerin. Zaten fonksiyon icinde bu deger ekrana yazdirilacak.
def matris_iz(mat,N) -> Void:
    T = 0 # toplam deger icin kullanilacak

    for i in range(0,N):
        for j in range(0,N):
            # eger bu kosul dogru ise o zaman
            # capraz bir eleman elde edilecek.
            if(i==j):
                T = T + mat[i][j]

    print("Bu matrisin izi: {}".format(T))

#matris girme
N=int(input("Kare matrisin tipini giriniz: "))
A=[[[] for i in range(N)] for j in range(N)] # aciklamaya bkz.
for i in range(N):
    for j in range(N):
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))

matris_iz(A,N)

# ------------------------------------------------------------------------------
# numpy kutuphanesini kullanarak(kitaptaki tekli python ornegi):
# ------------------------------------------------------------------------------
#matris izi
import numpy as np # numpy ile ilgili aciklama ornek 8_1 de mevcut
print("Matrisi [a b;c d] seklinde giriniz\n")
x=input()

A=np.matrix(x)
print("\nMatrisin izi: %d"%np.trace(A)) # np.trace icin bkz. aciklamaya
# Aciklama: https://numpy.org/doc/stable/reference/generated/numpy.trace.html
