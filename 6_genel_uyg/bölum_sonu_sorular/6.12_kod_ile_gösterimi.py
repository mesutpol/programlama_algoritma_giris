def convert_negative_to_positive(negative_number):
    if negative_number < 0:
        positive_number = -negative_number
        return positive_number
    else:
        return "Girilen sayı zaten pozitif."

# Örnek kullanım:

'''negative_number = -5
   print(convert_negative_to_positive(negative_number))'''