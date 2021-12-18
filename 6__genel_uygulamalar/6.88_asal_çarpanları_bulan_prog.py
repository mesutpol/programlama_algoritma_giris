# Asal Çarpanlar
a=int(input("pozitif tamsayı :")) ; b=2
while (a>1):
    if (a%b==0):
        print("%d\t"%b,end=''); a/=b
    else:
        b+=1
