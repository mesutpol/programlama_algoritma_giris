import tkinter
def hesap():
    r=int(E1.get())
    aci=int(E2.get())
    pi=3.14
    import math
    alan=(aci*pi*r**2)/360
    from tkinter import messagebox
    messagebox.showinfo("Daire dilimin alanı",alan)
        
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="Dairenin Yarıçapını Giriniz")
etiket1.grid(row=2,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="Daire diliminin açısını Giriniz")
etiket2.grid(row=3,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=3,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=2,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
