girilen_yazi = input("cümle girin: ")
yazinin_tersi = " "


def tersini_alma(yazi, tersi):
    for i in range(len(yazi) - 1, -1, -1):
        tersi += yazi[i]
    return tersi


kelimeler = []
for i in girilen_yazi.split(' '):
    kelimeler.append(tersini_alma(i, ""))

cumle_halinde_tersi = tersini_alma(girilen_yazi, yazinin_tersi)
kelime_halinde_tersi = " ".join(kelimeler)

print(
    """
    Cümlenin orjinali:                  {}
    
    Tamamen tersi alınmış hali:         {}
    
    Kelime kelime tersi alınmış hali:   {}
    
    """.format(girilen_yazi, cumle_halinde_tersi, kelime_halinde_tersi))