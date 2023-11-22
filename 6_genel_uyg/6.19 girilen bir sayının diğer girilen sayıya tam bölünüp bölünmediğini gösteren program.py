# Girilen bir sayinin diger girilen sayiya tam bolunup bolunmedigini gosteren program #

a = int(input("Enter a value"))
b = int(input("Enter a value"))

if (a % b == 0):
    print("a is divisible with b")   # a, b'ye tam bolunur
else:
    print("a is not divisible with b")   # a, b'ye tam bolunmez
