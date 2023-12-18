#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 17.12.2023

A=[] #Boş bir liste tanımladık

n=int(input("Bir 'n' değeri giriniz :")) #Kullanıcıdan 'n' değeri aldık

for i in range(0,n):#0 dan n değerine kadar döngü oluşturduk
    A.append(input("A(%d)="%(i+1)))#A dizisine ekledik

A.reverse()#A dizisinin elemanlarını ters çevirdik 'reverse()' ile yaptık
print(A) #A dizisini yazdırdık


