# Örnek 6.17
# İdeal transformatörün primer(giriş) tarafına ait gerilim, akım ve sarım sayısıyla sekonder(çıkış) tarafına ait gerilim girilmektedir.
# Buna göre transformatörün sekonder tarfına ait gerilim, akım ve güç değerlerini hesaplayıp türünü tespit ederek sonucu yazdıran program.

# Np, Primer sarım sayısıdır.
# Ns, Sekonder sarım sayısıdır.
# Vp, Primer sarımdan gelen voltaj değerinin karşılığıdır.
# Vs, Sekonder sarımdan giden voltaj değerinin karşılığıdır.
# Ip, Primer sarımdan gelen akım değerinin karşılığıdır.
# Is, Sekonder sarımdan giden akım değerinin karşılığıdır.
# Ps, Sekonder sarımdan giden güç değerinin karşılığıdır.

Vp = input("Primer Voltaj Değerini Girin:\n")
Ip = input("Primer Akım Değerini Girin:\n")
Np = input("Primer Sarım Değerini Girin:\n")
Ns = input("Sekonder Sarım Değerini Girin:\n")

Vs = Vp*Ns/Np
Is = Ip*Np/Ns
Ps = Vs*Is

print("Sekonder Sarımdan Giden Voltaj Değeri: ", Vs)
print("Sekonder Sarımdan Gider Akım Değeri: ", Is)
print("Sekonder Sarımdan Giden Güç Değeri: ", Ps)

if Vs > Vp:
    print("Kullanılan İdeal Transformatör Yükselticidir")
else:
    print("Kullanılan İdeal Transformatör Düşürücüdür.")
# Himmet Can Umutlu - November 28 - 2023