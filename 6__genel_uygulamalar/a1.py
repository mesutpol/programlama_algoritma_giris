import tkinter

def hesap():
    a=int(E1.get())
    r=int(E2.get())
    pi=3.14
    alan=a*pi*(r**2)/360

    etiket3.config(text=str(alan))
root = tkinter.Tk()
etiket1 = tkinter.Label(root,text="r giriniz giriniz")
etiket1.grid(row=1,column=0,padx=110, pady=10)

etiket2 = tkinter.Label(root,text="a giriniz")
etiket2.grid(row=3,column=0,padx=110, pady=10)

etiket3 = tkinter.Label(root,text="Sonuç")
etiket3.grid(row=4,column=0,padx=110, pady=10)

E1 = tkinter.Entry(root, bd =2)
E1.grid(row=3,column=1,padx=110, pady=3)

E2 = tkinter.Entry(root, bd =2)
E2.grid(row=1,column=1,padx=110,pady=3)


button1= tkinter.Button(root, text =" hesapla ",width=20,command=hesap)
button1.grid(padx=110, pady=70)

            
root.mainloop()
