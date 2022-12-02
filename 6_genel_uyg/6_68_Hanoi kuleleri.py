# Hanoi kuleleri
def hanoi(n,k,y,h):
  if (n==1):
    print("%d. disk: %s -> %s"%(n,k,h))
else:
  hanoi(n-1,k,h,y); print("%d. disk: %s -> %s"%(n,k,h))
  hanoi(n-1,y,k,h)
s=int(input("Disk sayısı: ")); hanoi(s,"Kaynak","Yardımcı","Hedef")  
