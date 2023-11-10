#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Kodu yaza Oğuzhan Demirbaş
#Kodun yazım tarihi 10.11.2023

while True:
    Deger=input("Sıcaklık değeri girin: ")

    if Deger.strip():#Girilen değeri kontrol et boş mu değil mi?
        try:
            t=float(Deger)#sıcaklığı ondalık sayıya çevir
            break#Geçerli bir değer alındığında döngüyü sonlandır
        except ValueError:#Eğer giriş  ondalık sayıya çevrilemezse, bu bir hata oluşturur ve kullanıcıya hata mesajı yazdırılır.
            print("Geçerli bir sayı giriniz!")
    else:
        print("Lütfen geçerli bir değer girin!")
if(t<0):
    print("Girdiğiniz değere göre madde 'KATI' halde")#Eğer sıcaklık 0'dan küçükse, maddenin "KATI" olduğu yazdırılır.
elif(t>0 and t<=100):
    print("Girdiğiniz değere göre madde 'SIVI' halde")#Eğer sıcaklık 0'dan büyük 100'e eşit ya da küçükse 'SIVI'maddenin olduğu yazdırılır
elif(t>100):
     print("Girdiğiniz değere göre madde 'GAZ' halde")#Eğer sıcaklık 100'den büyükse, maddenin "GAZ" olduğu yazdırılır.
            


# In[ ]:





# In[ ]:




