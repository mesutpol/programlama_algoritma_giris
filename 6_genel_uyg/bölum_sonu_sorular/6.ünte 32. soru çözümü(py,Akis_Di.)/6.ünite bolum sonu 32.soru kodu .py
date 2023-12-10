m=int(input("metre cinsinden dönüştürmek istediğiniz sayıyı giriniz : ")) 

x=int(input("\n1--Kilometreye dönüştürmek için\n2--Hektometreye dönüştürmek için\n3--Dekametreye dönüştürmek için\n4--Desimetreye dönüştürmek için\n5--santimetreye dönüştürmek için\n6--milimetreye dönüştürmek için\n1 den 6 ya kadar hangi birime döüştürmek isterseniz onu seçin : "))
if  x !=round(1,7):
    print("lütfen 1 ile 6 arası bir sayı seçin")
    

if x == 1 :
    km=m/1000
    print(f"metre cinsinden girilen sayının kilometremetre cinsinden gösterilişi : {km}","km")

if x == 2 :
    hm=m/100
    print(f"metre cinsinden girilen sayının Dekametremetre cinsinden gösterilişi : {hm}","hm")

if x == 3 :
    dam=m/10
    print(f"metre cinsinden girilen sayının dekametremetre cinsinden gösterilişi : {dam}","dam")

if x == 4 :
    dm=m*10
    print(f"metre cinsinden girilen sayının desimetremetre cinsinden gösterilişi : {dm}","dm")

if x == 5 :
    cm=m*100
    print(f"metre cinsinden girilen sayının santimetremetre cinsinden gösterilişi : {cm}","cm")

if x == 6 :
    mm=m*1000
    print(f"metre cinsinden girilen sayının milimetre cinsinden gösterilişi : {mm}","mm")

