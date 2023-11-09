
#Kodu yazan Savaş Mester
#Kodu Güncelleyen Oğuzhan Demirbaş
#Geliştirilme tarihi 10.11.2023

# Kullanıcıdan üç sayıyı giriş yapmasını isteyin
Say1 = input("Birinci sayıyı girin: ")
Say2 = input("İkinci sayıyı girin: ")
Say3 = input("Üçüncü sayıyı girin: ")

# Kullanıcının girişlerini boşlukları kaldırarak kontrol edin
if Say1.strip() and Say2.strip() and Say3.strip():
    # Girişler geçerli ise, her bir girişi ondalık sayıya dönüştürün
    Say1 = float(Say1)
    Say2 = float(Say2)
    Say3 = float(Say3)

    # En büyük, en küçük ve ortanca sayıları hesaplayın
    En_buyuk = max(Say1, Say2, Say3)
    En_kucuk = min(Say1, Say2, Say3)
    Ortanca = Say1 + Say2 + Say3 - En_buyuk - En_kucuk

    # Sıralanmış sonuçları yazdırın
    print("Büyükten küçüğe sıralama: \n {} \n {}\n {}".format(En_buyuk, Ortanca, En_kucuk))
else:
    # Geçerli sayılar girilmediğinde bir hata mesajı verin
    print("Geçerli sayılar girmeniz gerekmektedir.")







# In[ ]:




