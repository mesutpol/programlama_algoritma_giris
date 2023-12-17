#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 14.12.2023

# Boş listeler oluşturuldu
A=[]
B=[]
C=[]


n=int(input("Bir 'n' değeri giriniz :"))# Kullanıcıdan 'n' değeri alındı

for i in range(0,n): # 'n' defa dönen bir döngü

    # Kullanıcıdan A ve B listelerine değerler eklendi
    A.append(int(input("A(%d)="%(i+1))))
    B.append(int(input("B(%d)="%(i+1))))

    # Çarpım hesaplanıp C listesine ekleniyor
    carpim=A[i]*B[i]
    C.append(carpim)
print("\n")
# 'n' değerine kadar döngü kurduk C nin hem C(1),C(2) şeklinde yazılması hem de değerlerini çekmek için yaptık
for a in range(0,n):

  # Çarpımlar ekrana yazdırılıyor
  print("C(%d)=%d"%(a+1,C[a]))

