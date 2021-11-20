import tkinter
import calendar
def hesap():
  yil = int(E1.get())
  ay = int(E2.get())
  a=(calendar.month(yil, ay))
  
  etiket3.config(text=str(a))
root=tkinter.Tk()
root.configure(background='purple')
etiket1=tkinter.Label(root,text="Yıl giriniz")
etiket1.grid(row=0,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="Ay giriniz")
etiket2.grid(row=1,column=0,padx=110,pady=10)

etiket3=tkinter.Label(root,text="-------------")
etiket3.grid(row=4,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=0,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=1,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
root.mainloop()                      
    
