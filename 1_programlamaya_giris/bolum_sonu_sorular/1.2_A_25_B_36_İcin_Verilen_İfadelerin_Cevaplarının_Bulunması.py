# 1.2 A = 25 ve B = 36 için kodlanmış ifadelerin sonuçları.

A = 25      # A değişkenine '25' değerini tanımlıyoruz.

B = 36      # B değişkenine '36' değerini tanımlıyoruz

print("2. bölüm sonu sorusunda sorulan ifadeler aşağıdaki gibidir:\n")

print("1 = A ^ 1/2 + B ^ 1/2\n"
    "2 = A ^ (1/2) + B ^ 1/2\n"
    "3 = A ^ 1/2 + B ^ (1/2)\n"
    "4 = A ^ (1/2) + B ^ (1/2)\n"        # Kullanıcının istediği ifadeyi almak için ifadeleri numaralandırıyoruz.
    "5 = (A ^ 1/2 + B) ^ 1/2\n"
    "6 = (A ^ (1/2) + B) ^ 1/2\n"
    "7 = (A ^ (1/2) + B) ^ (1/2)\n"
    "8 = (A + B) ^ (1/2)\n")

ifade=input("Sonucunu öğrenmek istediğiniz ifadenin numarasını giriniz: ")       # Kullanıcının istediği ifadeyi alıyoruz.

if ifade == "1":       # Kullanıcı 1.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format(A ** 0.5 + B ** 0.5))        # 1.ifadenin cevabını yazdırır.
    
elif ifade == "2":     # Kullanıcı 2.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format(A ** (0.5) + B ** 0.5))      # 2.ifadenin cevabını yazdırır.

elif ifade == "3":     # Kullanıcı 3.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format(A ** 0.5 + B ** (0.5)))      # 3.ifadenin cevabını yazdırır.
    
elif ifade == "4":     # Kullanıcı 4.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format(A ** (0.5) + B ** (0.5)))    # 4. ifadenin cevabını yazdırır.
    
elif ifade == "5":     # Kullanıcı 5.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format((A ** 0.5 + B) ** 0.5))      # 5. ifadenin cevabını yazdırır.
    
elif ifade == "6":     # Kullanıcı 6.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format((A ** (0.5) + B) ** 0.5))    # 6. ifadenin cevabını yazdırır.
    
elif ifade == "7":     # Kullanıcı 7.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format((A ** (0.5) + B) ** (0.5)))    # 7.ifadenin cevabını yazdırır.
    
elif ifade == "8":     # Kullanıcı 8.ifadeyi seçmişse bu komut çalışacaktır.
    
    print("Seçtiğiniz ifadenin sonucu: {}".format((A+B) ** (0.5)))             # 8. ifadenin cevabını yazdırır.
    
else:                  # Geçerli olan değerlerden farklı bir değer girilirse bu komut çalışacaktır.
    
    print("Lütfen geçerli bir değer giriniz!")                                 # Kullanıcıdan geçerli bir değer girmesini ister.







