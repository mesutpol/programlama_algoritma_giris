import math
v=int(input("voltu giriniz="))
i=int(input("amperi giriniz="))
fi=int(input("dereceyi giriniz="))

fi=fi*math.pi/180
s=v*i
gf=math.cos(fi)
p=s*gf
q=s*math.sin(fi)

print("aktif güç\n",p)
print("reaktif güç\n",q)
print("görünür güç\n",s)
print("güç faktörü\n",gf)
