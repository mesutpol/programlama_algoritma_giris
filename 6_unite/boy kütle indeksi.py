a=eval(input("boyunuzu giriniz(cm)="))
b=int(input("cinsiyetiniz  [1-erkek / 2-kadın]="))
if(b==1):
    ik=50+2.3*(a/2.54-60);
else:
    ik=45.5+2.3*(a/2.54-60);
print("\nİdeal kilonuz (KG)= %0.2f"%ik);
