# newton raphson yöntemi
def f(x):
    return 3*x*x-12*x-4
def f1(x):
    return3*x*x-12*x-4
x0=eval(input("iterasyon başlangıç değeri: "))
h=eval(input("hassasiyet değeri: "))
x1=x0-f(x0)/f1(x0)
while (abs(f(x1))>h):
    x0=x1
    x1=x0-f(x0)/f1(x0)
print("\nKÖK: %0.10f"%x1)
