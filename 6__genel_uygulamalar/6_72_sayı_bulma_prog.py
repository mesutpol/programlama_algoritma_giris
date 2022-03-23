import random
tahmin=-1; s=0; bs=random.randint(1,99)
while (tahmin!=bs):
    tahmin=int(input("Tahmininiz: "))
    s=s+1
    if (tahmin>bs):
        print("Daha küçük sayı giriniz...\n")
    if (tahmin<bs):
        print("Daha büyük sayı giriniz...\n")
print("\n%d tahminde sayıyı buldunuz..."%s)
