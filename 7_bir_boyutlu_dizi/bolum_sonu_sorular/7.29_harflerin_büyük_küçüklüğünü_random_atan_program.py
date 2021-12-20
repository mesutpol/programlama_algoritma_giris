k = input( "kelime: ")
for i in range(len(k)) :
    if ((ord(k[i])>=65) & (ord(k[i])<=90)) :
        print("%c"%(ord(k[i])+32) , end='')
    else:
        print("%c"%(ord(k[i])-32) , end='')
