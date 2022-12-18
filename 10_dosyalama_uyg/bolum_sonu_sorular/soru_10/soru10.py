#soru10: Bir Bölümdeki Öğrencilerin Kişisel Bilgilerini tutan dosya uygulaması programı geliştiriniz
dosya=open('rehber.txt','a')
ad=input("Adı-Soyadı: ")
num =input("Öğrenci Numarası:")
tel =input("Telefonu :")
dosya.write(ad+"\t"+num+"\t"+tel+"\n")
dosya.close()