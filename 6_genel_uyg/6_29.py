a = int(input("a katsayısını giriniz:"))
b = int(input("b katsayısını giriniz:"))
c = int(input("c katsayısını giriniz:"))
if a==0:
    print("sıfıra bölünme hatası.")
else:
    if (a + b + c == 0):
        x1 = 1
        x2 = c / a
        print(x1, x2)
    else:
        x1 = (-b + ((b ** 2) - 4 * a * c)*(1 / 2)) / 2 * a
        x2 = (-b - ((b ** 2) - 4 * a * c)*(1 / 2)) / 2 * a
        print(int(x1),int(x2))

