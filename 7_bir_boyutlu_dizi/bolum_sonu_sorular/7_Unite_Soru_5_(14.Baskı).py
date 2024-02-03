#Kodu yazan Oğuzhan Demirbaş



'''istenen : Klavyeden girilen bir A dizisinin elemanlarını ters sıra ve işarette
   B dizisine aktaran programın python kodu'''



A=[]
B=[]

n=int(input("Kaç tane değer girmek istersiniz :"))

for i in range(0,n):
    A.append(int(input("Değer girin :")))
    B.append(-A[i])
B.reverse()
print(B)