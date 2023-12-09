#Yapan:Ramazan POLAT
#Tarih:09.12.2023
#Bölüm sonu 35. soru-->Ağırlık birimleri arasımda dönüşüm yapabilen programın akış diyagramını çizip kodlayınız. 


kg=float(input("Kilogram cinsinden dönüştürmek istediğiniz sayıyı giriniz:"))
x=int(input("\n1--Tona dönüştürmek için\n2--Kentala dönüştürmek için\n3--Hektogram dönüştürmek için\n4--Dekagram dönüştürmek için\n5--Grama dönüştürmek için\n6--Desigrama dönüştürmek için\n7--Santigrama dönüştürmek için\n8--Miligrama dönüştürmek için\n1'den 8'e kadar hangi birime döüştürmek isterseniz onu seçin : "))

if x!=round(1,9):
    print("1-8 arası sayı giriniz:")

if x==1:
    t=kg*1000
    print(f"Girilen değerin ton cinsinden karşılığı:{t}","ton")

if x==2:
    q=kg*100
    print(f"Girilen değerin kental cinsinden karşılığı:{q}","kental")

if x==3:
    hg=kg*0.1
    print(f"Girilen değerin hektogram cinsinden karşılığı:{hg}","hektogram")

if x==4:
    dak=kg*0.01
    print(f"Girilen değerin dekagram cinsinden karşılığı:{dak}","dekagram")

if x==5:
    g=kg*0.001
    print(f"Girilen değerin gram cinsinden karşılığı:{g}","gram")

if x==6:
    dg=kg*0.0001
    print(f"Girilen değerin desigram cinsinden karşılığı:{dg}","desigram")

if x==7:
    cg=kg*0.00001
    print(f"Girilen değerin santigram cinsinden karşılığı:{cg}","santigram")

if x==8:
    mg=kg*0.000001
    print(f"Girilen değerin miligram cinsinden karşılığı:{mg}","miligram")
