import tkinter
def hesap():
    h=int(E1.get())
    vo=int(E2.get())
    import math
    g=9.8
    t=(2*h/g)**(1/2)
    x=vo*t
    vy=g*t
    v=(vo**2+vy**2)**(1/2)
    from tkinter import messagebox
    messagebox.showinfo("Havada Kalma süresi",t)
    messagebox.showinfo("Yatayda aldığı yol",x)
    messagebox.showinfo("Yere çarpma hızı",v)
        
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="Yerden yüksekliğini giriniz(h)")
etiket1.grid(row=1,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="İlk hızını giriniz(vo)")
etiket2.grid(row=2,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=2,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=1,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
