#Kodu yazan Oğuzhan Demirbaş
#kodun yazılma tarihi 30.12.2023

#İstenen : Sıralı erişimli dosya yapısı kullanarak adres-telefon rehberi uygulaması geliştiriniz.


# Kullanıcıdan kaç kişi eklemek istediğini girmesini istedik
n=int(input("Kaç tane kullanıcı eklemek istersiniz :"))

# Kullanıcı etiketleri için bir sayaç yaptık. Her kişiye ait etiketi belirlemek için kullanılır.
hak=1

# "rehber.txt" adlı dosyayı "a" (append(ekleme)) modunda açar.
# Bu mod, dosyanın içeriğini korur ve mevcut içeriğin sonuna eklemeye izin verir.
# "utf8" encoding, dosyanın UTF-8 formatında olacağını belirtir.(Bu önemlidir yoksa türkçe karakter yazarsak okunmaz !)
dosya = open("rehber.txt", "a",encoding="utf8")

# Belirtilen sayıda kişi bilgisini almak için bir döngü başlatılır.
for i in range(1,n+1):

    # Dosyaya kullanıcı etiketini yazan bir satır eklenir.
    dosya.write(f"-{hak}.Kişi"+2*"\n")

    # Kullanıcıdan ad, soyad, telefon numarası ve adres bilgileri alınır.
    ad=input("Adınızı giriniz :")
    soyad=input("Soyad giriniz :")
    tel=input("Telefon numarası giriniz :")
    adres=input("Adres giriniz :")

    # Kullanıcının girdiği bilgiler dosyaya yazılır.
    dosya.write("\n"+ad+"\t"+soyad+"\n"+tel+"\n"+adres+3*"\n")

    # Her döngü adımında hak değeri arttırılarak bir sonraki kişi için etiketin benzersiz olması sağlanır(1,2,3 gibi).
    hak += 1

# Dosyayı kapatır ve değişiklikleri uygular. Bu, dosyanın düzgün bir şekilde işlenmesini sağlar.
dosya.close()
