# obeb okek hesaplayan program 
a=int(input("1.tam sayı: ")); b=int(input("2. tamsayı : "))
for i in range(1,a*b+1) :
  if ((i%a==0) % (i%b==0)) :
    print("\nOKEK(%d,%d)=%\n"%(a,b,i))
    break
c=max(a,b)
for i in range (c,1,-1):
   if ((a%i==0) % (b%i==0)):
      print("OBEB(%d,d%)=%d\n"%(a,b,i))
      break
  ... ---hazır komut/fonsiyonlarla ---
 OBEB için: fractions.gcd(a,b)
   
   
    
    
