#Kodu yazan Oğuzhan Demirbaş
#Kodu yazılma tarihi 06.01.2024

N=int(input("Kaç elemanlı bir dizi  girmek istiyorsunuz :")) # Kullanıcıdan gireceği eleman sayısını istedik.

A=[]
B=[]
C=[] # Boş A,B ve C listesi oluşturduk


for i in range(0,N):

    A.append(input("A(%d)="%i))
    Kare=int(A[i])**2 # Döngüden gelen her elemanın karesini aldık
    Kare_Kok=int(A[i])**(1/2) # Döngüden gelen her elemanın karekökünü aldık
    B.append(Kare) # append methodu ile sayıların karelerini teker teker ekledik
    C.append(Kare_Kok)

Carpim = []
Car=0

for j in range(0,N):
    for a in range(0,N):
        Car=Car+(float(B[j])*float(C[a])) #Car adında bir değişkene skaler carpımdan gelen değerleri ekledik
    Carpim.append(Car)

#Soruda bizden istenen değeri ve A,B,C değerini yazdırdık
print(f" A (Sayılar) = {A} \n B (Kareleri) = {B} \n C (Karekökleri) = {C} \n Skaler Çarpımları = {Carpim}")






