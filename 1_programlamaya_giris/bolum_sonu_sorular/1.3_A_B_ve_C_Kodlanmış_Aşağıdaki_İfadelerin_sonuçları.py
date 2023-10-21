#soruda verilen sayılar
A = 64
B = 16
C = 2

x =int(input("kaçıncı ifade(1 den 7 e kadar)"))

if x!=round(1,8):
   print("lütfen 1 ile 7 arası sayı girin")

#işlemlerin çalışması için yazılan kodlar


if x == 1:
    print(float(A**1/2+32/B*C+A/B**1/2)) #1.soru

if x ==2:
    print(float(A**(1/2)+32/B*C+A/B**1/2)) # 2.soru

if x == 3:
    print(float(A**(1/2)+32/(B*C)+A/B**1/2)) #3.soru
    
if x == 4:
   print(float(A**(1/2)+32/(B*C)+A/B**(1/2))) #4.soru

if x== 5:
   print(float(A**1/2+32/(B*C)+A/B**(1/2))) #5.soru

if x == 6:
   print(float(A**1/2+32/B*C+A/B**(1/2))) #6.soru
   
if x == 7:
    print(float(A**(1/2)+32/B*C+A/B**(1/2))) #7.soru     
        
   #burada kullanılınan ( ** ) üssü olarak kullanılır 
   #işlemlerde (1/2) şeklinde kullanılınca üssü olarak kullanılırken 1/2 şeklinde yazılanları sayının yarısı şeklinde alır
   