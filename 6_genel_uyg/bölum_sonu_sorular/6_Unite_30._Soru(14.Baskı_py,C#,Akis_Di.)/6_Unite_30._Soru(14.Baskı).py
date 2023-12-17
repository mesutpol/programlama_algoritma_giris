#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 13.12.2023
#Kod geliştirilerek geçen ay ve yıl değerleri de eklendi

import datetime#Date time kütüphanesini ekledik

dog_yılı=int(input("Doğum yılınızı giriniz :"))#Değişken tanımlamalarını yapıp kullanıcıdan değerler aldık
dog_gunu=int(input("Doğduğunuz günü giriniz :"))
dog_ayı=int(input("Doğum ayınızı giriniz :"))

bugun=datetime.datetime.today()#Today fonk. ile bugünün yıl,gün,ve ay değerlerini aldırdık

dogum_gunu=datetime.datetime(dog_yılı,dog_ayı,dog_gunu)#Date time modülündeki deltatime if. kullanmak için böyle tanımlama yaptık
#Tanımlamada (yıl,ay,gün) şek. doğum yılındaki değerleri yazdırdık.

sonuc=bugun-dogum_gunu#Sonuc if. de bize sadece gün bilgisi veriri
sonuc_yıl=bugun.year-dogum_gunu.year#(.year) ile bugünün ve doğum yılımızın yılları çağırılarak farkları alındı

print(f"Doğum gününüzden bugüne kadar {sonuc.days} gün geçmiştir"#Değerlerini formatlama yöntemi ile yazdırdık
      f"\nDoğum gününüzden bugüne kadar {sonuc_yıl*12} ay geçmiştir"#Eğer yaşımızı 12 ile çarparsak toplam geçen ayı hesaplamış oluruz
      f"\nDoğum gününüzden bugüne kadar {sonuc_yıl} yıl geçmiştir")

