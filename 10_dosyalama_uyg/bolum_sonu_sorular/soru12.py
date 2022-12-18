#Soru 12 : Bir Mağazadaki Ürünlerin Bilgisini Tutan Dosya Uygulamasını Geliştiriniz 
dosya =open('ürün.txt', 'a')
ad = input("Ürün Adını Giriniz : ")
cins = input("Ürünün Cinsini Giriniz : ")
fiyat = input("Ürünün Fiyatını Giriniz : ")
dosya.write(ad+"\t"+cins+"\t"+fiyat+"\n")
dosya.close()
