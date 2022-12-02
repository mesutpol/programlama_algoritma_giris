import tkinter
def hesap():
    g=10
    h=int(E1.get())
    vo=int(E2.get())
    t=(2*h/9.8)**(1/2)
    x=vo*t
    vy=9.8*t
    v=(vo**2+vy**2)**(1/2)
    

    etiket3.config(text=str(t))
    etiket4.config(text=str(x))
    etiket5.config(text=str(v))
root=tkinter.Tk()
root.configure(background='purple')
etiket1=tkinter.Label(root,text="cismin yerden yüksekliğini giriniz")
etiket1.grid(row=0,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="cismin ilk hızını giriniz")
etiket2.grid(row=1,column=0,padx=110,pady=10)

etiket3=tkinter.Label(root,text="cismin havada kalma süresi")
etiket3.grid(row=4,column=0,padx=110,pady=10)

etiket4=tkinter.Label(root,text="cismin yatayda aldığı yol")
etiket4.grid(row=7,column=0,padx=110,pady=10)

etiket5=tkinter.Label(root,text="cismin çarpma hızı")
etiket5.grid(row=10,column=0,padx=110,pady=10)



E1=tkinter.Entry(root,bd=2)
E1.grid(row=0,column=1,padx=110,pady=3)


E2=tkinter.Entry(root,bd=2)
E2.grid(row=1,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
root.mainloop()














