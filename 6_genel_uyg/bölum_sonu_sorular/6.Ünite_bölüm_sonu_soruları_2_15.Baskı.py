def find_triangle_type():
    side1 = float(input("1. kenarı giriniz: "))
    side2 = float(input("2. kenarı giriniz: "))
    side3 = float(input("3. kenarı giriniz: "))

    # Çizgiler aynı olursa
    if side1 == side2 == side3:
        return "Eşkenar Üçgen"
    # İki kenar aynı olursa
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "İkizkenar Üçgen"
    # Üçgen, yukarıda verilen kenarlarla oluşturulamaz
    elif side1!=side2 or side1!=side3 or side2!=side3:
        return "Çeşitkenar Üçgen"
    # İki kenarın toplamı diğer kenardan büyükse ve kenarlar eşkenar olmazsa
    else:
        return "Çıkışsız Üçgen"

print(find_triangle_type())