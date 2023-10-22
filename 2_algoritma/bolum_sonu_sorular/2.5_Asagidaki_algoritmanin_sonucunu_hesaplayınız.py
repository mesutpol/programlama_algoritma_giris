'''

Soru: Aşağıdaki algoritmanın sonucunu hesaplayınız

1 - Başla
2 - T=0
3 - S=0
4 - Eğer S>10 ise  Git 8
5 - T = T+2*S
6 - S+2
7 - Git 4
8 - Yaz T
9 - Dur.


Elbette bütün algoritmayı tek tek yazarak değil,
bu işi yapması için bir program kodlayarak bu işi yapacağız.

'''

#hadi başlayalım.

T = 0
# T'nin değerinin başlangıçta 0 olduğunu belirledik.
S = 0
# S'nin değerinin başlangıçta 0 olduğunu belirledik.


while True:
    
    
    '''

 while komutu türkçedeki anlamıyla "sırasında", tam da anlamı gibi çalışarak eğer bu iş sırasında
 eğer "S" sayısı 10 sayısından küçükse işleme devam edecektir, yalnız büyükse devam etmeyip işlemi yazdıracaktır.

 
 '''
    

    if S > 10: 
        # if komutu eğer demektir, tıpkı türkçesindeki gibi "eğer" şeklinde çalışır. burada ise S, 10'dan büyükse durur.
        S = 0
        # S
    T = T + 2 * S 
    S = S + 2

    if S <= 10:
        continue
    else:
        break

print(T)
# ve print komutu da olduğu gibi sonucu ekranı yazdırır.
# Bu sayede bu algoritmanın sonucu öğrenmiş oluruz
# (made by: Melih Aydınlı aka. foroxygenn 22.10.2023 - 02.51)