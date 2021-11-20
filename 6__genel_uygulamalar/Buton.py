from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Yusuf Vahit Kurtoğlu")
window.geometry("800x400")
def ButtonFunc():
 messagebox.showinfo( "404Error", "Başarısız")
B = Button(window, text ="Hata",height=10,width=50, command = ButtonFunc)
B.pack()
window.mainloop()
