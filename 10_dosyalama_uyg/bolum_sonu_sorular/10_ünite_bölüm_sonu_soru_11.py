#10.Ünite Bölüm Sonu Soru 11: Bir Bölümdeki Öğrencilerin Notlarını Tutan Dosya Uygulaması Programını Geliştiriniz
dosya =open('notlar.txt','a')
ad = input("Öğrenci Adı-Soyadı :")
no = input("Öğrencinin Notu :")
dosya.write(ad+"\t"+no+"\n")
dosya.close()