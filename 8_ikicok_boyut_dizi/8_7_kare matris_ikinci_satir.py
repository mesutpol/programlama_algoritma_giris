# Ornek 8.7
# Klavyeden girilen NxN tipindeki A matrisinin 2. satir elemanlarinin toplamini 
# bulan program.

# bu fonksiyon ikinci satirdaki matris degerlerinin toplamini bulup yazdiriyor.
# parametreler sirasiyla: deger listesi, kare matrisin tipi(mesela 2x2,3x3,4x4...)
def ikinci_satir(liste, matris:int)->None:  # return type 'None' cunku bulunan deger
                                            # yazdirilacak fonksiyon icinde
    T = 0 # son toplam deger icin degisken
    for i in range(matris): # her sutun icin
        T += liste[1][i] # T = A[1][i] + T

    print("Ikinci satirdaki matris elemanlarinin toplami {}".format(T))
    
#matris girme
N=int(input("Kare matrisin tipini giriniz: "))
A=[[[] for i in range(N)] for j in range(N)] # onceki orneklerdeki aciklamalara bkz.
for i in range(N): # satir icin
    for j in range(N): # sutun icin
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))

ikinci_satir(A,N) # fonksiyon burada cagirildi
