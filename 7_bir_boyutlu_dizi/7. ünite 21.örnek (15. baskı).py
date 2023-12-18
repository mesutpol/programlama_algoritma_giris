A=[]
n=int(input("sınıfın kişi sayısını giriniz : "))
for i in range (0,n):
    print("(%d) numaralı kişinin aldığı not :"%(i+1))
    A.append(int(input()))
t=0
for i in range (0,n):
    t=t+A[i]
ort=t/n
for i in range (0,n):
    if (A[i]<ort):
        print("(%d) numaralı kişi:"%(i+1),"kaldı ")
    else:
        print("(%d) numaralı kişi:"%(i+1),"geçti ")
        

#N kişililk bi sınıfın bir dersten yıl sonu notu girilmektedir buna göre sınıf ort üstünde
#olan kişilere(geçti) geçemyenlere ise (kaldı) yazdıran program

        