import tkinter
def hesap():
    a=int(E1.get())
    Radyan=a*(3/180)
    Gradyan=a*200/180
    
    from tkinter import messagebox
    messagebox.showinfo("Radyan cinsinden",Radyan)
    messagebox.showinfo("Gradyan cinsinden",Gradyan)
    
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="Derece Giriniz")
etiket1.grid(row=0,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=3,column=0,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
    
