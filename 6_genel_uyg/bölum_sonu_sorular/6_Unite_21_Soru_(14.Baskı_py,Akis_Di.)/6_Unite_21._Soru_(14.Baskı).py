#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 28.11.2023

import math
try:
    ilk_terim=float(input("İlk terimi giriniz :"))
    son_terim=float(input("Son terimi giriniz :"))
    ortak_fark=int(input("Ortak farkı giriniz :"))
    e_degeri=math.e


    x=(ilk_terim-son_terim)/ortak_fark+1
    #1.Denkleme göre çözüm
    hsp_1=(e_degeri**x)/math.cos(x)
    print(f"1.Denkleme göre çözülmüş değer {hsp_1}")
    #2.Denkleme göre çözüm
    hsp_2=2*math.cos(x)+3*math.sin(x)+4*(e_degeri**x)
    print(f"2.Denkleme göre çözülmüş değer {hsp_2}")
    #3.Denkleme göre çözüm
    hsp_3=math.cos(x)/math.sin(x)
    print(f"3.Denkleme göre çözülmüş değer {hsp_3}")
except ValueError:
    print("Geçerli bir değer giriniz !")





