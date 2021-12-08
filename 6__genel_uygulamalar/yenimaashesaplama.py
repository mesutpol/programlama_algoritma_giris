yeniMaas = 0
maas = input("Maaşı Gir : ")
zam = input("Zam Oranı(%) : ")
yeniMaas = int(maas) + (int(maas) * int(zam) / 100)
print("Zamlı Maaş :", yeniMaas)