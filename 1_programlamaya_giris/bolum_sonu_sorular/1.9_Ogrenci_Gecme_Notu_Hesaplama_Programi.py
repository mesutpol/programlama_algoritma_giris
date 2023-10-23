# Bir sınıftaki öğrencilerden ancak Matematik (mt) ile Türkçe (Tr) notu 50'ye eşit veya üzerinde olup
# Fizik (Fzk) veya Tarih (Th) derslerinin herhangi birisinden notu 50'ye eşit veya üzerinde olanlar
# "Başarılı" Sayılmaktardır.
try:
    mt = float(input("Matematik Notu: "))
    tr = float(input("Türkçe Notu: "))
    fzk = float(input("Fizik Notu: "))
    th = float(input("Tarih Notu: "))
    if mt >= 50 and tr >= 50 and (fzk >= 50 or th >= 50):
        print("Başarılı")
    else:
        print("Başarısız")
except ValueError: #Eğer kullanıcı sayı yerine harf veya başka bir karakter girerse
    print("Geçersiz bir sayı girdiniz.") #Ekrana hata mesajı yazdırıyoruz.