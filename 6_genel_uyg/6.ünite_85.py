#Karekök(2)
t=1;n=eval (input("Bölme sayısı: "))
for i in range(n) :
    t=2+1/t
    print("Karekök(2)=%f"%(1+1/t))