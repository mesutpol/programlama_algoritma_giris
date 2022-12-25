sayi=int(input("Sayıyı girin"))
if sayi>1:
   for i in range(2,sayi):
        if (sayi %i)==0:
            print(sayi," Asal sayi değildir.")
            break
   else:
      print(sayi,"Asal sayidir.")
else:
  
   print(sayi,"Asal sayi değildir.")
