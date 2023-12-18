#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 17.12.2023

n=input("Bir cümle giriniz :")
C=[] # C listesi, "C(i)=harf" formatında yazdırdık
B=[] # B listesi, 'n' cümledeki karakterleri içerir

# Her harfi C ve B listelerine ekledik
for i in range(0,len(n)):
    C.append("C(%d)=%s"%(i+1,n[i])) # Burada C(i)=harf formatında ekledik sırayla indexe göre
    B.append(n[i]) # Burada 'n' cümledeki karakterleri ekledik sırayla indexe göre

if(len(n)%2==0):
    for s in range(0,len(n),2):
         if(s+1<len(n)):
            C[s],C[s+1]=C[s+1],C[s] # C listesindeki elemanları indekslere göre takas etme
            B[s],B[s+1]=B[s+1],B[s] # B listesindeki elemanları da indekslere göre takas etme

# Eğer cümle tek uzunluktaysa, sonuna boş bir karakter ekleyerek işlemi sürdürme
elif(len(n)%2==1):

    C.append("C(%d)=%s"%(len(n)," ")) # C dizisine boşluk ekledik
    B.append(" ") #B dizisine boşluk ekledik

    for s in range(0, len(n)+1, 2): #0 dan başlat n'nin uzunluğuna kadar 2 şer 2 şer atla
        if (s + 1 < len(n)+1): #Burda boşluk da eklediğimiz için 'len(n)+1' formatında yazdık
            C[s], C[s + 1] = C[s + 1], C[s] # C listesindeki elemanları indekslere göre takas etme
            B[s], B[s + 1] = B[s + 1], B[s] # B listesindeki elemanları da indekslere göre takas etme


# Sonuçları yazdırdık
print(C,"\n",B)
