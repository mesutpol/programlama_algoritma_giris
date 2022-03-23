# Faktoriyel
def faktoriyel(k):
  if (k<=1):
    return 1
  else:
    return k*faktoriyel(k-1)
  a=int(input("Pozitif tamsayı: ")); print("\n%d!=%d"%(a,faktoriyel(a)))
