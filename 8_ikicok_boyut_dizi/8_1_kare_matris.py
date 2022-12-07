# Ornek 8.1
# Klavyeden coklu verinin girilmesi ve NxN tipinde bir A matrisine yerlestirilmesi

# Kitaptaki ornek 1
#matris girme
N=int(input("Kare matrisin tipini giriniz: "))
A=[[[] for i in range(N)] for j in range(N)] # aciklamaya bkz.
for i in range(N):
    for j in range(N):
        A[i][j]=int(input("A(%d,%d= "%(i+1,j+1)))
# Aciklama:
# A = [ [bir bos deger olustur her bir N satir girdi icin] degerini olustur her bir N kolon girdi icin]
# Mesela, 2 denilirse
# [ [bos deger] [bos deger] ]
# [ [bos deger] [bos deger] ]
# gibi liste icinde bos degerli bir 2x2 matris listesi olusturacak.

# Kitaptaki ornek 2
#matris girme
import numpy as np
x=input("Matrisi [a b;c d] seklinde giriniz\n")
A=np.matrix(x)
# Aciklama: NumPy, Python programlama dili için bir kütüphanedir ve büyük, çok
# boyutlu diziler ve matrisler için destek ve bu diziler üzerinde çalışmak için
# geniş bir üst düzey matematiksel fonksiyon koleksiyonu ekler.
# Burada numpy kutuphanesinden 'np' modulunu ilk eklendi. Sonraki satirda kulla-
# nicidan veri alindi. Daha sonra ise np cagirildi x verisi ile.
