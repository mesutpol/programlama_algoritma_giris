import tkinter
def hesap():
    
   m=int(E1.get())
   v=int(E2.get())
   h=int(E3.get())
   g=10
   Ep=m*g*h
   Ek=1/2*m*v**2
   A=Ep+Ek


   etiket4.config(text=str(A))
root=tkinter.Tk()
root.configure(background='purple')
etiket1=tkinter.Label(root,text="cismin kütlesi")
etiket1.grid(row=0,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="cismin hızı")
etiket2.grid(row=1,column=0,padx=110,pady=10)

etiket3=tkinter.Label(root,text="cismin yerden yüksekliği")
etiket3.grid(row=2,column=0,padx=110,pady=10)

etiket4=tkinter.Label(root,text="------")
etiket4.grid(row=5,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=0,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=1,column=1,padx=110,pady=3)

E3=tkinter.Entry(root,bd=2)
E3.grid(row=2,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
root.mainloop()
