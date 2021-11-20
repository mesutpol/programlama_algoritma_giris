import tkinter
def hesap():
    m=int(E1.get())
    v=int(E2.get())
    h=int(E3.get())
    import math
    ep=m*9.8*h
    ek=m*v**2/2
    from tkinter import messagebox
    messagebox.showinfo("Potansiyel Enerjisi",ep)
    messagebox.showinfo("Kinetik Enerjisi",ek)
        
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="Maddenin kütlesini giriniz")
etiket1.grid(row=1,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="Maddenin hızını giriniz")
etiket2.grid(row=2,column=0,padx=110,pady=10)

etiket3=tkinter.Label(root,text="Maddenin yerden yüksekliğini giriniz")
etiket3.grid(row=3,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=3,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=2,column=1,padx=110,pady=3)

E3=tkinter.Entry(root,bd=2)
E3.grid(row=1,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
