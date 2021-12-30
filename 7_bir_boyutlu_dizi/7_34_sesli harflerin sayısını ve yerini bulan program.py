# Sesli harfler
b="aeiloöuü"; s=0; yer=[]; c=input("cümle: ")
for i range(len(c)):
  if (c[i] in b):
    s+=1; yer.append(i+1)
    print("\nCümlede %d tane sesli harf vardır.\nYerleri:"%s);print(yer)
