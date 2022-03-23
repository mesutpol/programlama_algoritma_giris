# Euler yöntemi
x0=eval(input("x(0): ")); y0=eval(input("y(0): "))
h=eval(input("Adım değeri: ")); n=int(input("değer sayısı: "))
x=x0; y=y0; print("\nSonuçlar (x,y)"); print("%f\t%f"%(x,y))
for i in range(n):
  y+=h*(-y/(2+x)); x+=h; print("%f\t%f"%(x,y))
