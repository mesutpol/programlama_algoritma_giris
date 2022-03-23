def tarak_siralama(a):
  gap=len(a)
  degisim=1
  while ((gap!=1) or (degisim==1)):
      gap=int(gap/1.3)
      if (gap<1):
          gap=1
      degisim=0
      for i in range(0,len(a)-gap):
          if(a[i]>a[i+gap]):
             a[i],a[i+gap]=a[i+gap],a[i]
             degisim=1
print("Diziyi [a b c d] şeklinde giriniz!")
a=[int(i) for i in input () .split ()]
print("\nsıralı dizi:\n------------")
tarak_siralama(a)
for i in range(len(a)):
  print("%d\t"%a[i],end='')
