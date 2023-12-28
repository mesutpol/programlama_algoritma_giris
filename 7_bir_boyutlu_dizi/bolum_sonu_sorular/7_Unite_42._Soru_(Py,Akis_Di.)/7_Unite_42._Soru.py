#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 28.12.2023

'''Klavyeden girilen mesajın karakterlerini ASCII tamsayı karşılıklarını
   10 tabanında yazdıran programın akış diyagramını çizip kodlayın'''

n=input("Dönüştürmek istediğiniz Mesajınızı girin :") # Kullanıcıdan bir metin girişi alınır ve n değişkenine atanır.
B=[] # ASCII değerlerini tutmak için boş bir liste oluşturulur.
A=list(n) # Girilen metni karakterlerine ayırmak için list() fonksiyonu kullanıldı

for i in range(0,len(n)): # Her bir karakterin ASCII değerini hesaplamak için bir döngü başlatılır.
    Don_Ascii=ord(A[i]) # ord() fonksiyonu ile karakterin ASCII değeri hesaplanır.
    B.append(Don_Ascii) # Hesaplanan ASCII değeri B listesine eklenir.
print(B) # Oluşturulan B listesi ekrana yazdırılır.

