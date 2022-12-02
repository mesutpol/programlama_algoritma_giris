# #giriline karakterin baş harfini büyük yazmak için kullanılır
# str.capitalize('browing')  #sonuç Browing
# 'browing'.capitalize()  #sonuç Browing

# #fonksiyondaki karakter dizesini alır
# str.center('Sonnet 43', 26) 
# #sonuç ('        Sonnet 43         ')

# #dizideki terim sayısını gösterir
# str.count('How do I love thee? Let me count the ways.', 'the')
# #sonuç (2)

# #name error çünkü isim tanımalanmadı
# import math
# help(math.sqrt())


# #karakter içindeki harflerin bulma
# 'species'.startswith('a')  #false çünkü 'a' harfi yok
# 'species'.startswith('spe') #true çünkü 'spe' karekterde mevcut
# #.endswits fonksiyonu ile karekter bulma
# 'species'.endswith('a') #false çünkü 'a' harfi karakterde yok
# 'spacies'.endswith('es')  #true çünkü 'es' karekteri mevcut

# #ilk harf küçük diğer harfleri büyük yazma
# 'Computer Science'.swapcase() #sonuç 'cOMPUTER sCIENCE'

# #.format fonksiyonu ile süslü parentezleri doldurma
# '"{0}" is derived from "{1}"'.format('none','one none') #sonuç "none" is derived from "one none"'
# '"{0}" is derived from the {1} "{2}"'.format('etymology','greek','ethos') #sonuç '"Etymology" is derived from the Greek "ethos"'

# #önce baş harfi küçültüp diğer harfleri büyüttük sonra ise karekter aradık
# 'Computer Science'.swapcase().endswith('ENCE') #sonuç true

# #iki karekteri toplama
# 'TTA' + 'GGG' #sonuç 'TTAGGG' 
# 'TTA'.__add__('GGG') #sonuç aynı


# #girilen sayının mutlak değerini alma
# abs(-3)  #sonuç '3'
# (-3).__abs__() #sonuç '3'
# 3+5  #sonuç '8'
# 3 ._add_(5) #sonuç '8'
 
# 3>5 #false
# 3 .__gt__(5) #false


