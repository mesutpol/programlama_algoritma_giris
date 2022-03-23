# Bitsel İşlemler
a=int(input ("Pozitif tamsayı: "))
k=int(input("Kaçincı bit: "))
print("\nYazma: %d"%(a| (1<< (k-1) )))
print("Silme: %d"%(a&(~(1<< (k-1) ))))
print ("Tümleme: %d"% (a^ (1<<(k-1))))
