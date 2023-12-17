import math
A=[]         #A ve B adında iki boş liste oluşturulur. Bu listeler, kullanıcı tarafından girilecek değerleri içerecek.
B=[]
n=int(input("Bir 'n' değeri girin : "))  #Kullanıcıdan bir tamsayı olan n değerini girmesini ister.
for i in range (0,n):    #0'dan n'e kadar olan sayıları içeren bir döngü ile kullanıcıdan A ve B listelerinin elemanlarını alır.
    A.append(int(input("A(%d)="%(i+1))))   
    B.append(int(input("B(%d)="%(i+1))))
t1=t2=t3=t4=t5=0
c1=c2=1
for i in range(0,n):   #Bir döngü ile çeşitli matematiksel hesaplamalar yapılır.
    t1=t1+A[i]**2
    t2=t2+A[i]*B[i]
    t3=t3+B[i]
    t4=t4+A[i]
    t5=t5+math.log(B[i])
    c1=c1*(B[i])**(1/2)
    c2=c2*A[i]
f=(t1+2*t2+t3**2+3*c1)/(t4**(1/2)+n*t5-c2)  #Belirli bir formüldeki hesaplamalar gerçekleştirilir ve sonuç f değişkenine atanır.
print(f"işlemin sonucunu : {f}")  #Hesaplanan sonucu ekrana yazdırır.