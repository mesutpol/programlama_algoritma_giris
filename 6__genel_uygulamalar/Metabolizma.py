import math
import tkinter

def hesap():
    k=int(E1.get())
    b=int(E2.get())
    y=int(E3.get())
    c=int(E4.get())

    #harris-benedict denklemi
    if(c==1):
        hb=655.0955+9.5634*k+1.8496*b-4.6756*y
    else:
        hb=66.473+13.7516*k+5.0033*b-6.775*y
    

    #schofield denklemi
    if(c==1):
        if(10<=y<=17):
            pb=692.6+13.384*k
        elif(18<=y<=29):
            pb=486.6+18.818*k
        elif(30<=y<=59):
            pb=845.6+8.126*k
        elif(60<=y):
            pb=658.5+9.082*k
    else:
        if(10<=y<=17):
            pb=658.2+17.686*k
        elif(18<=y<=29):
            pb=692.2+15.057*k
        elif(30<=y<=59):
            pb=873.1+11.472*k
        elif(60<=y):
            pb=587.7+11.711*k
    

    #owen denklemi
    if(c==1):
        ow=795+7.18*k
    else:
        ow=879+10.2*k
    

    #Mifflin-St Jeor denklemi
    if(c==1):
        ms=9.99*k+6.25*b-4.92*y-161
    else:
        ms=9.99*k+6.25*b-4.92*y-5
    

    #Dsö pratik hesaplama formülü
    if(c==1):
        dso1=22.8*k
    else:
        dso1=24*k
   

    #dsö detaylı

    if(c==1):
        if(18<=y<=30):
           dso2=496+14.7*k
        elif(31<=y<=60):
            dso2=829+8.7*k
        elif(61<=y):
            dso2=596+10.5*k
    else:
        if(18<=y<=30):
            dso2=679+15.3*k
        elif(31<=y<=60):
            dso2=879+11.6*k
        elif(61<=y):
            dso2=487+13.5*k
  

    #dsö en detaylı

    if(c==1):
        if(18<=y<=30):
           dso3=35+13.3*k+334*(b/100)
        elif(31<=y<=60):
            dso3=865+8.7*k-25*(b/100)
        elif(61<=y):
            dso3=-302+9.2*k+637*(b/100)
    else:
        if(18<=y<=30):
            dso3=717+15.4*k-27*(b/100)
        elif(31<=y<=60):
            dso3=901+11.3*k+16*(b/100)
        elif(61<=y):
            dso3=-1071+8.8*k+1128*(b/100)
    if(c==1):
        if(1000<=hb,pb,ow,ms,dso1,dso2,dso3<=1400):
            from tkinter import messagebox
            messagebox.showinfo("harika","olması gerektiği gibi")
        else:
            from tkinter import messagebox
            messagebox.showinfo("üzgünüm","iyi değil")
    else:
        if(1200<=hb,pb,ow,ms,dso1,dso2,dso3<=1600):
            from tkinter import messagebox
            messagebox.showinfo("harika","olması gerektiği gibi")
        else:
            from tkinter import messagebox
            messagebox.showinfo("üzgünüm","iyi değil")
 

    etiket5.config(text=str(hb))
    etiket6.config(text=str(pb))
    etiket7.config(text=str(ow))
    etiket8.config(text=str(ms))
    etiket9.config(text=str(dso1))
    etiket10.config(text=str(dso2))
    etiket11.config(text=str(dso3))

root=tkinter.Tk()
etiket1=tkinter.Label(root,text="kilonuzu giriniz")
etiket1.grid(row=0,column=0,padx=50, pady=5)

etiket2=tkinter.Label(root,text="boyunuzu giriniz")
etiket2.grid(row=1,column=0,padx=50, pady=5)

etiket3=tkinter.Label(root,text="yaşınızı giriniz")
etiket3.grid(row=2,column=0,padx=50, pady=5)

etiket4=tkinter.Label(root,text="cinsiyetiniz [1-Erkek / 2-Kadın]")
etiket4.grid(row=3,column=0,padx=50, pady=5)

etiket5=tkinter.Label(root,text="harris-benedict denklemine göre")
etiket5.grid(row=0,column=2,padx=50, pady=5)

etiket6=tkinter.Label(root,text="schofield denklemine göre")
etiket6.grid(row=1,column=2,padx=50, pady=5)

etiket7=tkinter.Label(root,text="owen denklemine göre")
etiket7.grid(row=2,column=2,padx=50, pady=5)

etiket8=tkinter.Label(root,text="Mifflin-St Jeor denklemine göre")
etiket8.grid(row=3,column=2,padx=50, pady=5)

etiket9=tkinter.Label(root,text="Dünya Sağlık Örgütü pratik sonucu")
etiket9.grid(row=4,column=2,padx=50, pady=5)

etiket10=tkinter.Label(root,text="Dünya Sağlık Örgütü kısmî sonucu")
etiket10.grid(row=5,column=2,padx=50, pady=5)

etiket11=tkinter.Label(root,text="Dünya Sağlık Örgütü sonucu")
etiket11.grid(row=6,column=2,padx=50, pady=5)
             
E1=tkinter.Entry(root, bd=1)
E1.grid(row=0,column=1,padx=50,pady=5)

E2=tkinter.Entry(root, bd=1)
E2.grid(row=1,column=1,padx=50,pady=5)

E3=tkinter.Entry(root, bd=1)
E3.grid(row=2,column=1,padx=50,pady=5)

E4=tkinter.Entry(root, bd=1)
E4.grid(row=3,column=1,padx=50,pady=5)


button1=tkinter.Button(root,text="hesapla",width=20,command=hesap)
button1.grid(padx=50,pady=10)


root.configure(background='purple')
