whales[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[1]

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[1001]

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales[-1]     #=3


whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
third=whales[2]
print('Third day:', third)

krypton = ['Krypton', 'Kr', -157.2, -153.4]
krypton[1] #"kr"
krypton[2]#-157.2

nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
nobles[1] #="neon"

name="darwin"
capitalized=name.upper()
print(capitalized)    #sonuç=DARWİN


half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
len(half_lives) #sonuç=5
max(half_lives)  #sonuç=37330.0
min(half_lives)   #sonuç=14
sum(half_lives)   #sonuç=404864.7 bütün değerleri topla
sorted(half_lives)  #sonuç=[14, 887.7, 6563.0, 24100.0, 373300.0] sayıları küçükten büyüğe sıralar
   
#karekter eklemek için yapılması gereken   
orginal['h','he','li'] 
final=orginal+['be'] 
print(final) 
#sonuç=['h','he','li','be']   

#girilen değeri 3kere çarpar
metals=['fe','ni']
metals*3

#karakter dizesinden  terim silme
metals['fe','ni']
del metals[0]
#sonuç=['ni']


#girilen elementlerden gas olan elementi seçer
nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
gas=input('enter a gas:')
sonuç=argon


#fonksiyon içinden karakter şeçme
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_phenotypes[:4]
sonuç=['emb','him','unc','lon']
celegans_phenotypes[4:]
#sonuç=['Dpy', 'Sma']

#fonksiyonu eski haline getirme
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
remove_last_item(celegans_markers)
sonuç=['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']


#karekter dizesine karakter ekleme
#1.extend() ile ekleme
colors=['red','orange','green']
colors.extend(['black','blue'])
colors #sonuç=['red', 'orange', 'green', 'black', 'blue']

#.apped() ile ekleme
colors.append('purple')
colors  #sonuç['red', 'orange', 'green', 'black', 'blue', 'purple']

#.insert() ile ekleme
colors.insert(2,'yellow')
colors  #sonuç=['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple'] 


#.remove()ile ekleme
colors.remove('black')
colors  #sonuç=[['red', 'orange', 'yellow', 'green', 'blue', ['purple']]]


