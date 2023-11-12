#0-255 arası girilen bir tam sayının ASCII kod karşılığını ekrana yazdıran programın akış diyagramını çizip yazılımını yapınız.
try:
    sayı=int(input("0-255 arası bir sayı giriniz:"))
    if(sayı>=0 and sayı<=255):
        asciikod=chr(sayı)
        print(f"sayının ascıı kodu:{asciikod}")
    else:
        print("Aralığa dikkat edin 0-255")
except ValueError:
    print("Tanımlı aralık giriniz!")