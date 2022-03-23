# McCarthy 91
def mc91(k):
    if (k>100):
        return k-10
    else:
        return mc91(mc91(k+11))
 n=int(input("değer: "))
 print("\nMcCarthy 91 fonksiyon değeri: %d\n"%mc91(n))
