import math
import tkinter
def hesap():
    a=int(E1.get())
    b=int(E2.get())
    aci=int(E3.get())
    c=(a^2+b^2-2*a*b*Cos(aci*3.14/180))^(1/2)
 
root=tkinter.Tk()
root.configure(background="black")

etiket1=tkinter.Label(root,text="birinci kenar")
etiket1.grid(row=0,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="ikinci kenar")
etiket2.grid(row=1,column=0,padx=180,pady=30)

etiket3=tkinter.Label(root,text="aci")
etiket3.grid(row=2,column=0,padx=180,pady=30)

etiket4=tkinter.Label(root,text="üçüncü kenar")
etiket4.grid(row=3,column=0,padx=180,pady=30)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=0,column=1,padx=110,pady=10)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=1,column=1,padx=110,pady=10)

E3=tkinter.Entry(root,bd=2)
E3.grid(row=2,column=1,padx=110,pady=10)



button1 =tkinter.Button(root, text = " hesapla " , width=10,height=3, command=hesap)
button1.grid(padx=110, pady=80)

