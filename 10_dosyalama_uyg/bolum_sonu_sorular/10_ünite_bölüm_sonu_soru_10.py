#10.Ünite Bölüm Sonu Soru 10: Bir Bölümdeki Öğrencilerin Kişisel Bilgilerini Tutan Dosya Uygulaması Programını Geliştiriniz
dosya =open('rehber.txt','a')
ad = input("Öğrenci Adı-Soyadı :")
num = input("Öğrencinin Numarası :")
tel = input("Öğrencinin Telefonu : ")
dosya.write(ad+"\t"+num+"\t"+tel+"\n")
dosya.close()