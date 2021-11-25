#parçalı fonksiyon
x=eval(input("x noktasını giriniz: "))
if(x<0):
    y=1
elif((0<=x)&(x<=2)):
    y=x
elif((2<x)&(x<=4)):
    y=3
else:
    y=4-x
print("fonksiyonun x=%0.2f noktasındaki değeri=%0.2f\n"%(x,y))
