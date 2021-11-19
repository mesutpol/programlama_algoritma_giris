
import tkinter
def hesap():
    a=int(E1.get())
    radyan=a*3.14/180
    gradyan=a*200/180
 
    etiket3.config(text=str(radyan))
    etiket5.config(text=str(gradyan))
root=tkinter.Tk()
root.configure(background="black")


etiket1=tkinter.Label(root,text="dereceyi giriniz")
etiket1.grid(row=0,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="radyan")
etiket2.grid(row=2,column=0,padx=180,pady=30)

etiket3=tkinter.Label(root,text="------")
etiket3.grid(row=2,column=1,padx=180,pady=30)

etiket4=tkinter.Label(root,text="gradyan")
etiket4.grid(row=3,column=0,padx=110,pady=10)

etiket5=tkinter.Label(root,text="-------")
etiket5.grid(row=3,column=1,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=0,column=1,padx=110,pady=10)



button1 =tkinter.Button(root, text = " hesapla " , width=10,height=3, command=hesap)
button1.grid(padx=110, pady=80)


