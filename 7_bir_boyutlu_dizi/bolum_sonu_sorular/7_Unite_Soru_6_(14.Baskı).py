#Kodu yazan Oğuzhan Demirbaş


'''istenen : Klavyeden girilen N değerine göre  tek indisli elemanları '0'
çift indisli elemanları '1' olan N elemanlı bir A dizisi oluşturan programın python kodu'''

A=[]

n=int(input("Girilecek değer sayısı :"))
for i in range(0,n):
    if i%2==0:
        A.append(1)
    elif i%2==1:
        A.append(0)
print(A)

