import math
import tkinter
def hesap():
    a=int(E1.get())
    b=int(E2.get())
    aci=int(E3.get())
    c=(a**2+b**2-2*a*b*math.cos(aci*3.14/180))**(1/2)

    etiket4.config(text=str(c))

root=tkinter.Tk()
etiket1=tkinter.Label(root,text="birinci kenarı giriniz")
etiket1.grid(row=0,column=0,padx=150,pady=15)

etiket2=tkinter.Label(root,text="ikinci kenarı giriniz")
etiket2.grid(row=1,column=0,padx=150,pady=15)

etiket3=tkinter.Label(root,text="aradaki açıyı giriniz")
etiket3.grid(row=2,column=0,padx=150,pady=15)

etiket4=tkinter.Label(root,text="")
etiket4.grid(row=3,column=0,padx=150,pady=15)

E1=tkinter.Entry(root, bd=2)
E1.grid(row=0,column=1,padx=150,pady=15)

E2=tkinter.Entry(root, bd=2)
E2.grid(row=1,column=1,padx=150,pady=15)

E3=tkinter.Entry(root, bd=2)
E3.grid(row=2,column=1,padx=150,pady=15)



button1=tkinter.Button(root, text="üçüncü kenarı hesapla", width=20, command=hesap)
button1.grid(padx=150, pady=60)
