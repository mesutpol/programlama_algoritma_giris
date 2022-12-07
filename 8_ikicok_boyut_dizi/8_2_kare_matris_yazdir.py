# Ornek 8.2
# NxN tipindeki A kare matrisinin elemanlarinin ekrana yazdirilmasi.

# Kitaptaki ornek
#matris girme
for i in range(N):
    for j in range(N):
        print("A(%d,%d)= %d"%(i,j,A[i][j]))
        # mesela ornek cikti "A(0,2) = 5". ayr.bkz. aciklamaya.
# Aciklama: ayrica print("A({0},{1})= {3}".format(i,j,A[i][j])) seklinde
# yazilabilir istenilirse.

