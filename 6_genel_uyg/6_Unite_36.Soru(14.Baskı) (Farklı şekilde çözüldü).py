#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 28.11.2023
#Kodun amacı:Klavyeden girilen kilo,boy,yaş ve cinsiyete göre "Bazal metabolizma hızı"'nı hesaplama
try:
    kg=float(input("Kilonuzu girin (kg) :"))#Değişken tanımlamalarını yaptık
    boy=float(input("Boyunuzu girin (cm) :"))
    yas=int(input("Yaşınızı girin tam sayı olarak :"))
    #Harris Benedict denklemi
    print("\n Cinsiyet seçimi \n1--Kadın\n2--Erkek")
    cinsiyet=int(input("Cinsiyet seciniz (E/K) :"))#string veri tipini intager veri tipine dönüştürdük.

    print("Bir değer giriniz !")
    print("-" * 50)#Satıra 50 tane '-' yazdırdık okunurluğu arttırmak için.
    print("Harris Benedict denklemine göre çözülmüştür")
    if cinsiyet==1:
        hsp_k=655.0955+9.5634*kg+1.8496*boy-4.6756*yas
        print("-"*50)
        print("Bazal Metabolizma Hızı :",hsp_k)
    elif cinsiyet==2:
         hsp_er=66.473+13.7516*kg+5.0033*boy-6.775*yas
         print("Bazal Metabolizma Hızı :",hsp_er)
    #Schofield denklemine göre çözüm
    print("-"*50)
    print("Schofield denklemine göre çözülmüştür")
    if cinsiyet==1:
        if 10<yas<=17:
            hsp_k=692.6+13.384*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 18<yas<=29:
            hsp_k=486.6+14.818*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 30<yas<=59:
            hsp_k=845.6+8.126*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 60<=yas:
            hsp_k=658.5+9.082*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
    elif cinsiyet==2:
        if 10<yas<=17:
            hsp_er=658.2+17.686*kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 18<yas<=29:
            hsp_er=692.2+15.057*kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 30<yas<=59:
            hsp_er=873.1+11.472*kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 60<=yas:
            hsp_er=587.7+11.711*kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        #Owen denklemi
        print("-" * 50)
        print("denklemine göre çözülmüştür")
        if cinsiyet==1:
            hsp_k=795+7.18*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif cinsiyet==2:
            hsp_er=879+10.2*kg
            print("Bazal Metabolizma Hızı :", hsp_er)
    #Mifflin-St jeor denklemi
    print("-" * 50)
    print("Mifflin-St jeor denkelmine göre çözülmüştür ")
    if cinsiyet==1:
        hsp_k=9.99*kg+6.25*boy-4.92*yas-161
        print("Bazal Metabolizma Hızı :", hsp_k)
    elif cinsiyet==2:
        hsp_er=9.99*kg+6.25*boy-4.92*yas+5
        print("Bazal Metabolizma Hızı :", hsp_er)
    #Dünya sağlık örgütü denk.
    print("-" * 50)
    print("Dünya sağlık örgütü pratik denklemine göre çözülmüştür")
    if cinsiyet==1:
        hsp_k=22.8*kg
        print("Bazal Metabolizma Hızı :", hsp_k)
    elif cinsiyet==2:
        hsp_er=24*kg
        print("Bazal Metabolizma Hızı :", hsp_er)
    #Dünya sağlık örgütü (WHO/FAO/UNU)
    #1.Kısım
    print("-" * 50)
    print("Dünya sağlık örgütü (WHO/FAO/UNU) 1.Kısım")
    if cinsiyet==1:
        if 18<yas<=30:
            hsp_k=496+14.7*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 31<yas<=60:
            hsp_k=829+8.7*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 61<=yas:
            hsp_k=596+10.5*kg
            print("Bazal Metabolizma Hızı :", hsp_k)
    elif cinsiyet==2:
        if 18 < yas <= 30:
            hsp_k = 679 + 15.3 * kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 31 < yas <= 60:
            hsp_k = 879 + 11.6 * kg
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 61 <= yas:
            hsp_k = 487 + 13.5 * kg
            print("Bazal Metabolizma Hızı :", hsp_er)
    # Dünya sağlık örgütü (WHO/FAO/UNU)
    # 2.Kısım
    print("-" * 50)
    print("Dünya sağlık örgütü (WHO/FAO/UNU) 2.Kısım")
    boy_m=boy/100#cm değerini metreye çevirdik
    if cinsiyet==1:
        if 18<yas<=30:
            hsp_k=35+13.3*kg+334*boy_m
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 31<yas<=60:
            hsp_k=865+8.7*kg-25*boy_m
            print("Bazal Metabolizma Hızı :", hsp_k)
        elif 61<=yas:
            hsp_k=-302+9.2*kg+637*boy_m
            print("Bazal Metabolizma Hızı :", hsp_k)
    elif cinsiyet==2:
        if 18 < yas <= 30:
            hsp_k = 717+15.4*kg-27*boy_m
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 31 < yas <= 60:
            hsp_k = 901+11.3*kg+16*boy_m
            print("Bazal Metabolizma Hızı :", hsp_er)
        elif 61 <= yas:
            hsp_k = -1071+8.8*kg+1128*boy_m
            print("Bazal Metabolizma Hızı :", hsp_er)
except ValueError:#Kullanıcının boş değer girmemesi için hata mesajı döndürdük
    print(" Geçerli bir değer giriniz !")






