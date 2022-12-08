# Ornek 8.6
# Klavyeden girilen NxN tipindeki A matrisinin yedek kosegen uzerindeki
# elemnalarinin toplamini bulan program.


# matrisin bulundugu degisken "mat", matrisin tipi "N"
# None kullanildi return type icin cunku geriye getirmesine gerek yok
# bulunan degerin. Zaten fonksiyon icinde bu deger ekrana yazdirilacak.
def matris_kose(mat,N) -> None:
    T = 0 # toplam deger icin kullanilacak

    for i in range(0,N):
        for j in range(0,N):
            # eger bu kosul dogru ise o zaman
            # capraz bir eleman elde edilecek.
            if(i+j==N-1):
                T = T + mat[i][j]

    print("Bu matrisin yedek kosegeni uzerindeki elemanlarin toplami: {}".format(T))

#matris girme
N=int(input("Kare matrisin tipini giriniz: "))
A=[[[] for i in range(N)] for j in range(N)] # aciklamaya bkz.
for i in range(N):
    for j in range(N):
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))

matris_kose(A,N)
