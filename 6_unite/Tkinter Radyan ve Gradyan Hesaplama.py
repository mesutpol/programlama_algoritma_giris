import tkinter
def hesap():
    a=int(E1.get())
    Radyan=a*(3/180)
    Gradyan=a*200/180
    
    etiket2.config(text=str(Radyan))
    etiket3.config(text=str(Gradyan))
    
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="Dereceyi Giriniz")
etiket1.grid(row=0,column=1,padx=110,pady=10)

etiket2=tkinter.Label(root,text="Radyan Cinsinden Sonucu")
etiket2.grid(row=2,column=0,padx=110,pady=10)
etiket3=tkinter.Label(root,text="Gradyan Cinsinden Sonucu")
etiket3.grid(row=4,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=3,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
    
