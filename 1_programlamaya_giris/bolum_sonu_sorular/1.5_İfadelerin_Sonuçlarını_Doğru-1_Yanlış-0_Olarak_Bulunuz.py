#1.Bölüm sonu soruları 5.soru

#Soruda verilen değerleri veriyoruz
A = 5 
B = 6 
C = 7 
D = 8 

#Kullanıcı İfadeleri rahatca seçebilmesi için ekrana yazdırıyoruz 
print("""Bir ifade seçiniz: 
1. (A>B) ve (C<D) 
2. (A<B) ve ((C<=D) veya (A>D)) 
3. ((D>B) veya (C>A)) ve ((A<C) veya (C>D))  
4. ((D<=B) veya (C>A)) ve ((not (A>D)) veya (B>C)) 
5. DEĞİL (DEĞİL (DEĞİL (C>D))) 
6. DEĞİL ((A>B) veya (B>D)) veya (A>D) 
7. DEĞİL (DEĞİL ((A>D) ve (DEĞİL (A<D) ve (DEĞİL (C>B))) ve (DEĞİL (A>=C)))""")

#Kullanıcıdan hangi soruyu seçmek istediğini soruyoruz
sayi = int(input("Kaçıncı ifade (Sadece 1 ile 7 arası sayı giriniz.): "))

#Kullanıcının yazaıcağı sayıları kısıtlıyoruz
if sayi < 1 or sayi > 7  :           
        print("Geçerli bir sayı giriniz (1 ile 7 arasında).")

#Ve seçtiği ifade doğru ise 1 yanlış ise 0 gösteriyoruz
elif sayi == 1:
    if (A > B) and (C < D):
        print("Sonucu: 1")
    else:
        print("Sonucu: 0")
elif sayi == 2:
    if (A < B) and (((C <= D) or (A > D))):
        print("Sonucu: 1")
    else:
        print("Sonucu: 0")
elif sayi == 3:
    if ((D > B) or (C > A)) and ((A < C) or (C > D)):
        print("Sonucu: 1")
    else:
        print("Sonucu: 0")
elif sayi == 4:
    if ((D <= B) or (C > A)) and ((not (A > D)) or (B > C)):
        print("Sonucu: 1")
    else:
        print("Sonucu: 0")
elif sayi == 5:
    if not (not (not (C > D))):
        print("Sonucu: 1")
    else: 
        print("Sonucu: 0")
elif sayi == 6:
    if (not (A > B) or (B > D)) or (A > D):
        print("Sonucu: 1")
    else: 
        print("Sonucu: 0")
elif sayi == 7:
    if not (not ((A > D) and (not (A < D) and (not (C > B)) and (not (A >= C))))):
        print("Sonucu: 1")
    else:
        print("Sonucu: 0")
#MertAlii